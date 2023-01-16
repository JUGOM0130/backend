"""
コード体系操作　バックエンドファイル


"""
from fastapi import APIRouter
from pydantic import BaseModel
import mysql.connector as mycon     # SQL接続
import CONST                        # 共通定数ファイル
import datetime as dt               # 日付
import logging


router = APIRouter(
    prefix='/code_taikei',
    tags=['code_taikei']
)


class CodeTaikei(BaseModel):
    ctkind: int
    cthead: str
    ctenumber: str
    ctnumber: int
    ctfoot: str


class GetNewNumber(BaseModel):
    ctkind: int
    cthead: str
    ctenumber: str
    ctfoot: str


@router.get('/read/{kind}')
def read(kind: int):
    cnx = None
    try:
        cnx = mycon.connect(
            user=CONST.CONST['user'],  # ユーザー名
            password=CONST.CONST['pw'],  # パスワード
            host=CONST.CONST['host']  # ホスト名(IPアドレス）
        )
        if cnx.is_connected:
            logging.debug("connected")
        cursor = cnx.cursor(dictionary=True)
        if kind == 0:
            select_sql = """
                SELECT * FROM a_system.m_code;
            """
        else:
            select_sql = f"""
                SELECT * FROM a_system.m_code WHERE ctkind = {kind};
            """
        cursor.execute(select_sql)
        mcode_list = cursor.fetchall()
        return mcode_list

    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"message": e}
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


@router.post('/regist')
def regist(req: CodeTaikei):
    cnx = None
    try:
        cnx = mycon.connect(
            user=CONST.CONST['user'],  # ユーザー名
            password=CONST.CONST['pw'],  # パスワード
            host=CONST.CONST['host']  # ホスト名(IPアドレス）
        )
        if cnx.is_connected:
            logging.debug("connected")
        cursor = cnx.cursor()
        isreg_sql = """
            SELECT
            *
            FROM
                a_system.m_code
            WHERE
                m_code.ctkind = %s
                AND m_code.cthead = %s
                AND m_code.ctnumber = %s
                AND m_code.ctenumber = %s
                AND m_code.ctfoot = %s
        """
        cursor.execute(isreg_sql, (req.ctkind, req.cthead,
                       req.ctnumber, req.ctenumber, req.ctfoot))
        isdata = cursor.fetchall()
        # データが登録されているかの判定
        logging.debug(isdata)
        if len(isdata) > 0:
            return {"message": "既にデータが登録されています。"}
        else:
            reg_sql = '''
                    INSERT INTO `a_system`.`m_code`
                    (`ctkind`,
                    `cthead`,
                    `ctenumber`,
                    `ctnumber`,
                    `ctfoot`)
                    VALUES(%s,%s,%s,%s,%s);
            '''
            data = [
                (req.ctkind, req.cthead, req.ctenumber, req.ctnumber, req.ctfoot,),
            ]
            cursor.executemany(reg_sql, data)
            rowcnt = cursor.rowcount
            cnx.commit()
            cnx.close()
            cursor.close()
            return {"message": f"{rowcnt} Inserted"}
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"message": e}
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


@router.post('/get_new_no')
def getNewNo(req: GetNewNumber):

    cnx = None
    try:
        cnx = mycon.connect(
            user=CONST.CONST['user'],  # ユーザー名
            password=CONST.CONST['pw'],  # パスワード
            host=CONST.CONST['host'],  # ホスト名(IPアドレス）
            database=CONST.CONST['db']  # データベース名
        )

        cursor = cnx.cursor()

        get_no_sql = """
            SELECT
                MAX(m_code.ctnumber) as number
            FROM
                a_system.m_code
            WHERE
                m_code.ctkind = %s
                AND m_code.cthead = %s
                AND m_code.ctenumber = %s
                AND m_code.ctfoot = %s
        """

        # タプルで指定
        data = (
            req.ctkind,       # コード種別No
            req.cthead,       # コードヘッダ
            req.ctenumber,    # 英番
            req.ctfoot,       # 末尾No
        )

        cursor.execute(get_no_sql, data)
        maxnumber_list = cursor.fetchone()
        cursor.close()

        number = maxnumber_list[0]
        if number:
            return {"max_number": number+1}
        else:
            return {"max_number": 1}

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()
