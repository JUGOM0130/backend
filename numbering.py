from fastapi import APIRouter
from pydantic import BaseModel
import mysql.connector as mycon

router = APIRouter(
    prefix='/saiban',
    tags=['saiban']
)


class Numbering(BaseModel):
    id: str
    number: int
    name: str
    biko: str


CONSTR = {
    'user': 'admin',
    'pw': '0000',
    'host': '192.168.0.20',
    'db': 'a_system'
}


@router.post('/create')
def createNumber(request: Numbering):
    cnx = None
    try:
        cnx = mycon.connect(
            user=CONSTR['user'],  # ユーザー名
            password=CONSTR['pw'],  # パスワード
            host=CONSTR['host']  # ホスト名(IPアドレス）
        )
        if cnx.is_connected:
            print("Connected!")
        cursor = cnx.cursor()
        sql = '''
                INSERT INTO `a_system`.`m_numbering`
                (`id`,`no`,`name`,`biko`)
                VALUES(%s,%s,%s,%s);
        '''
        data = [
            (request.id, request.number, request.name, request.biko),
        ]
        cursor.executemany(sql, data)
        cnx.commit()
        print(cursor)
        return {"message": f"{cursor.rowcount} Inserted"}
        cursor.close()
    except Exception as e:
        print(f"Error Occurred: {e}")
        return {"message": e}
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


@router.put('/update')
def updateNumber():
    return {'message': f'update'}


@router.get('/read')
def readNumber():
    cnx = None
    try:
        cnx = mycon.connect(
            user=CONSTR['user'],  # ユーザー名
            password=CONSTR['pw'],  # パスワード
            host=CONSTR['host'],  # ホスト名(IPアドレス）
            database=CONSTR['db']  # データベース名
        )

        cursor = cnx.cursor()

        sql = ('''
            SELECT `m_numbering`.`id`,
            `m_numbering`.`no`,
            `m_numbering`.`name`,
            `m_numbering`.`biko`,
            `m_numbering`.`toroku`,
            `m_numbering`.`kosin`
            FROM `a_system`.`m_numbering`;
        ''')
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()

        res = []
        for d in data:
            temp = {
                "id": d[0],
                "number": d[1],
                "name": d[2],
                "biko": d[3]
            }
            res.append(temp)

        return {"data": res}

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


@router.delete('/delete')
def deleteNumber():
    return {'message': f'delete'}
