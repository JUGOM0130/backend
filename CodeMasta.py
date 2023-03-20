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
    ckind: int
    chead: str
    cenumber: str
    cnumber: int
    cfoot: str


class GetNewNumber(BaseModel):
    ckind: int
    chead: str
    cenumber: str
    cfoot: str


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
                SELECT
                    `m_code`.`cid`,
                    `m_code`.`ckind`,
                    `m_code`.`chead`,
                    `m_code`.`cenumber`,
                    `m_code`.`cnumber`,
                    `m_code`.`cfoot`,
                    `m_parts`.`pname`,
                    `m_parts`.`pid`
                FROM
                    `a_system`.`m_code` LEFT JOIN `a_system`.`m_parts`
                        ON `m_code`.`cid` = `m_parts`.`pcid`
            """
        else:
            select_sql = f"""
                SELECT
                    `m_code`.`cid`,
                    `m_code`.`ckind`,
                    `m_code`.`chead`,
                    `m_code`.`cenumber`,
                    `m_code`.`cnumber`,
                    `m_code`.`cfoot`,
                    `m_parts`.`pname`,
                    `m_parts`.`pid`
                FROM
                    `a_system`.`m_code` LEFT JOIN `a_system`.`m_parts`
                        ON `m_code`.`cid` = `m_parts`.`pcid`
                WHERE
                    m_code.ckind = {kind};
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
    logging.debug(req)
    cnx = None
    try:
        cnx = mycon.connect(
            user=CONST.CONST['user'],  # ユーザー名
            password=CONST.CONST['pw'],  # パスワード
            host=CONST.CONST['host'],  # ホスト名(IPアドレス）
            auth_plugin='mysql_native_password'
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
                m_code.ckind = %s
                AND m_code.chead = %s
                AND m_code.cnumber = %s
                AND m_code.cenumber = %s
                AND m_code.cfoot = %s;
        """
        cursor.execute(isreg_sql, (req.ckind, req.chead,
                       req.cnumber, req.cenumber, req.cfoot))
        isdata = cursor.fetchall()
        # データが登録されているかの判定
        logging.debug(isdata)
        if len(isdata) > 0:
            return {"message": "既にデータが登録されています。"}
        else:
            reg_sql = '''
                    INSERT INTO `a_system`.`m_code`
                    (`ckind`,
                    `chead`,
                    `cenumber`,
                    `cnumber`,
                    `cfoot`)
                    VALUES(%s,%s,%s,%s,%s);
            '''
            data = [
                (req.ckind, req.chead, req.cenumber, req.cnumber, req.cfoot,),
            ]
            cursor.executemany(reg_sql, data)
            rowcnt = cursor.rowcount
            cnx.commit()
            new_idx = 0
            status = "OK"
            message = ""
            if req.ckind == 1:
                if req.cnumber == 9999:
                    EN = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                    for idx, en in enumerate(EN):
                        if en == req.cenumber:
                            new_idx = idx + 1
                    # template の英番を一つ進める
                    update = '''
                        UPDATE `a_system`.`m_code_template`
                        SET `ctenumber` = %s
                        WHERE `ctkind` = %s
                            AND `cthead` = %s;
                    '''
                    data = (EN[new_idx], req.ckind, req.chead)
                    cursor.execute(update, data)
                    status = "100"
            elif req.ckind == 2:
                if req.cnumber == 999:
                    new_enum = ""
                    cenum = req.cenumber
                    EN = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                    if cenum[1] != "Z":
                        for idx, en in enumerate(EN):
                            if en == cenum[1]:
                                new_idx = idx + 1
                                new_enum = cenum[0] + EN[new_idx]
                    else:
                        for idx, en in enumerate(EN):
                            if en == cenum[0]:
                                new_idx = idx + 1
                                new_enum = EN[new_idx] + "A"

                    # template の英番を一つ進める
                    update = '''
                        UPDATE `a_system`.`m_code_template`
                        SET `ctenumber` = %s
                        WHERE `ctkind` = %s
                            AND `cthead` = %s;
                    '''
                    data = (new_enum, req.ckind, req.chead)
                    cursor.execute(update, data)
                    status = "200"
            elif req.ckind == 3:
                if req.cenumber == 9999:
                    logging.debug("繰り上げ処理が必要だが処理を作成していない")
                    status = "300"

            else:
                print()
            cnx.commit()
            cnx.close()
            cursor.close()
            return {"result": {"message": f"{rowcnt} Inserted\n"+message, "status": status}}
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"message": e}
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


@router.post('/get_new_no_select_list')
def getNewNoSelectList(req: GetNewNumber):
    logging.debug(req)
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
                MAX(m_code.cnumber) as number
            FROM
                a_system.m_code
            WHERE
                m_code.ckind = %s
                AND m_code.chead = %s
                AND m_code.cenumber = (SELECT m_code_template.ctenumber
                                        FROM m_code_template
                                        WHERE m_code_template.ctkind = %s
                                            AND m_code_template.cthead = %s)
                AND m_code.cfoot = %s
        """

        # タプルで指定
        data = (
            req.ckind,       # コード種別No
            req.chead,       # コードヘッダ
            req.ckind,       # コード種別No
            req.chead,       # コードヘッダ
            req.cfoot,       # 末尾No
        )

        cursor.execute(get_no_sql, data)
        maxnumber_list = cursor.fetchone()
        cursor.close()

        number = maxnumber_list[0]
        logging.debug(maxnumber_list)
        if number:
            return {"max_number": number+1}
        else:
            return {"max_number": 1}

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


@router.post('/get_new_no_input_direct')
def getNewNoInputDirect(req: GetNewNumber):
    logging.debug(req)
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
                MAX(m_code.cnumber) as number
            FROM
                a_system.m_code
            WHERE
                m_code.ckind = %s
                AND m_code.chead = %s
                AND m_code.cenumber = %s
                AND m_code.cfoot = %s
        """

        # タプルで指定
        data = (
            req.ckind,       # コード種別No
            req.chead,       # コードヘッダ
            req.cenumber,    # 英番
            req.cfoot,       # 末尾No
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
