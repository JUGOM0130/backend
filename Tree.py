from fastapi import APIRouter
from pydantic import BaseModel
import datetime as dt               # 日付
import logging
from typing import Union
import MysqlConnector
import mysql.connector
router = APIRouter(
    prefix='/tree',
    tags=['tree']
)

reg_sql = """
    INSERT INTO `a_system`.`t_tree_table`
    (`tree_id`,
    `composition_id`,
    `parts_id`,
    `toroku`,
    `kosin`)
    VALUES
    (<{tree_id: }>,
    <{composition_id: }>,
    <{parts_id: }>,
    <{toroku: CURRENT_TIMESTAMP}>,
    <{kosin: CURRENT_TIMESTAMP}>);

"""


class TreeRegistData(BaseModel):
    tree_id:int
    composition_id:int
    parts_id:int

@router.get('/get_root_list')
def getRootList():
    sql = """
    SELECT
        `m_parts`.`pid`,
        `m_parts`.`pcd`,
        `m_parts`.`pname`
    FROM `a_system`.`m_parts`;
    """
    try:
        
        mci = MysqlConnector.Connector()
        cursor = mci.get_cursor()
        print(type(cursor))
        cursor.execute(sql)
        data = cursor.fetchall()
        rowcnt = cursor.rowcount

        logging.debug(data)

        return {"result": {"status": "OK", "message": f"{rowcnt} getDatas", "data": data}}
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"result": {"status": "ERR", "message": f"Error Occurred: {e}"}}
    finally:
        mci.close()
        
@router.post('/tree_regist')
def tree_regist(td:TreeRegistData):
    print("")