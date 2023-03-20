
import logging
import datetime as dt               # 日付
import CONST                        # 共通定数ファイル
import mysql.connector as mycon     # SQL接続
from pydantic import BaseModel
from fastapi import APIRouter
from typing import Union
SELECT = """
    SELECT `m_code_template`.`ctid`,
        `m_code_template`.`ctkind`,
        `m_code_template`.`cthead`,
        `m_code_template`.`ctenumber`
    FROM `a_system`.`m_code_template`
        """
INSERT = """
    INSERT INTO `a_system`.`m_code_template`
    (`ctkind`,`cthead`,`ctenumber`)
    VALUES
    (%s,%s,%s)
"""
IS_DATA = """
    SELECT `m_code_template`.`cthead`
    FROM `a_system`.`m_code_template`
    WHERE `m_code_template`.`cthead` = %s
    AND `m_code_template`.`ctkind` = %s;

"""


router = APIRouter(
    prefix='/code_template',
    tags=['code_template']
)


class CodeTemplate(BaseModel):
    ctkind: Union[int, None]
    cthead: Union[str, None]


@router.post('/regist')
def regist(req: CodeTemplate):
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
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(IS_DATA, (req.cthead, req.ctkind,))
        isdata = cursor.fetchone()
        # データが登録されているかの判定
        if isdata != None:
            logging.debug("既にデータが登録されています。")
            return {"result": {"status": "ERR", "message": "既にデータが登録されています"}}
        else:
            if req.ctkind == 1:
                cursor.execute(INSERT, (req.ctkind, req.cthead, "A"))
            elif req.ctkind == 2:
                cursor.execute(INSERT, (req.ctkind, req.cthead, "AA"))
            elif req.ctkind == 3:
                cursor.execute(INSERT, (req.ctkind, req.cthead, ""))
            else:
                cnx.close()
                cursor.close()
                return {"result": {"status": "ERR", "message": f"ctkind={req.ctkind}はありません確認してください"}}
            rowcnt = cursor.rowcount
            cnx.commit()
            cnx.close()
            cursor.close()
            return {"result": {"status": "OK", "message": f"{rowcnt} Inserted"}}
    except Exception as e:
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


@router.get('/select')
def select():
    cnx = None
    try:
        cnx = mycon.connect(
            user=CONST.CONST['user'],  # ユーザー名
            password=CONST.CONST['pw'],  # パスワード
            host=CONST.CONST['host']  # ホスト名(IPアドレス）
            ,auth_plugin='mysql_native_password'
        )
        if cnx.is_connected:
            logging.debug("connected")
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(SELECT)
        data = cursor.fetchall()
        rowcnt = cursor.rowcount
        cnx.commit()
        cnx.close()
        cursor.close()
        return {"result": {"status": "OK", "message": f"{rowcnt} getDatas", "data": data}}
    except Exception as e:
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


"""
@router.post('/update')
def update(req: CodeTemplate):
    logging.debug(req)
    cnx = None
    try:

        cnx = mycon.connect(
            user=CONST.CONST['user'],  # ユーザー名
            password=CONST.CONST['pw'],  # パスワード
            host=CONST.CONST['host']  # ホスト名(IPアドレス）
        )
        if cnx.is_connected:
            logging.debug("\tconnected")
        cursor = cnx.cursor()
        cursor.execute(UPDATE, (req.pname,
                                req.ppname,
                                req.prevision,
                                req.pvendor,
                                req.ptype,
                                req.pmaterial,
                                req.pio,
                                req.pmtlmain_cost,
                                req.pmtlsub_cost,
                                req.pprocdict_cost,
                                req.pprocsub_cost,
                                req.pid,))
        cnx.commit()
        cnx.close()
        cursor.close()
        return {"message": "Update Ok"}
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"message": e}
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()
"""
