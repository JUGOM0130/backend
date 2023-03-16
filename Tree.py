from fastapi import APIRouter
from pydantic import BaseModel
import mysql.connector as mycon     # SQL接続
import CONST                        # 共通定数ファイル
import datetime as dt               # 日付
import logging


router = APIRouter(
    prefix='/tree',
    tags=['tree']
)


@router.get('/get_root_list')
def getRootList():
    sql = """
    SELECT
        `m_parts`.`pid`,
        `m_parts`.`pcd`,
        `m_parts`.`pname`
    FROM `a_system`.`m_parts`;
    """
    cnx = None
    try:
        cnx = mycon.connect(
            user=CONST.CONST['user'],  # ユーザー名
            password=CONST.CONST['pw'],  # パスワード
            host=CONST.CONST['host'],  # ホスト名(IPアドレス）
            database=CONST.CONST['db']  # データベース名
        )

        cursor = cnx.cursor(dictionary=True)
        cursor.execute(sql)
        data = cursor.fetchall()
        rowcnt = cursor.rowcount
        cursor.close()

        logging.debug(list)

        return {"result": {"status": "OK", "message": f"{rowcnt} getDatas", "data": data}}
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()
