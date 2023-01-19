
import logging
import datetime as dt               # 日付
import CONST                        # 共通定数ファイル
import mysql.connector as mycon     # SQL接続
from pydantic import BaseModel
from fastapi import APIRouter
from typing import Union
SELECT = """SELECT `m_parts`.`pid`,
                `m_parts`.`pctid`,
                `m_parts`.`pcd`,
                `m_parts`.`pname`,
                `m_parts`.`ppname`,
                `m_parts`.`prevision`,
                `m_parts`.`pvendor`,
                `m_parts`.`ptype`,
                `m_parts`.`pmaterial`,
                `m_parts`.`pio`,
                `m_parts`.`pmtlmain_cost`,
                `m_parts`.`pmtlsub_cost`,
                `m_parts`.`pprocdict_cost`,
                `m_parts`.`pprocsub_cost`
            FROM `a_system`.`m_parts`;
        """
INSERT = """
        INSERT INTO `a_system`.`m_parts`
        (`pctid`,
        `pcd`,
        `pname`,
        `ppname`,
        `prevision`,
        `pvendor`,
        `ptype`,
        `pmaterial`,
        `pio`,
        `pmtlmain_cost`,
        `pmtlsub_cost`,
        `pprocdict_cost`,
        `pprocsub_cost`)
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
"""
IS_DATA = """
            SELECT `m_parts`.`pid`
            FROM `a_system`.`m_parts`
            WHERE `m_parts`.`pctid` = %s;
"""


router = APIRouter(
    prefix='/parts',
    tags=['parts']
)


class Parts(BaseModel):
    pid: Union[int, None]
    pctid: Union[int, None]
    pcd: Union[str, None]
    pname: Union[str, None]
    ppname: Union[str, None]
    prevision: Union[str, None]
    pvendor: Union[str, None]
    ptype: Union[str, None]
    pmaterial: Union[str, None]
    pio: Union[str, None]
    pmtlmain_cost: Union[int, None]
    pmtlsub_cost: Union[int, None]
    pprocdict_cost: Union[int, None]
    pprocsub_cost: Union[int, None]


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
def regist(req: Parts):
    logging.debug(req)
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
        cursor.execute(IS_DATA, (req.pctid,))
        isdata = cursor.fetchall()
        # データが登録されているかの判定
        logging.debug(isdata)
        if len(isdata) > 0:
            logging.debug("既にデータが登録されています。")
            return {"message": "既にデータが登録されています。"}
        else:
            cursor.execute(INSERT, (req.pctid,
                                    req.pcd,
                                    req.pname,
                                    req.ppname,
                                    req.prevision,
                                    req.pvendor,
                                    req.ptype,
                                    req.pmaterial,
                                    req.pio,
                                    req.pmtlmain_cost,
                                    req.pmtlsub_cost,
                                    req.pprocdict_cost,
                                    req.pprocsub_cost))
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
