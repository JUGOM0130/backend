#!python3.11
# サーバー起動　uvicorn main:app --reload
# 400 Bad Request :　どこのIPから許可するかを設定で解決
# 422 Unprocessable Entity : 型が理解できないエラー（バリデーションを設けてあげる
# クラスに指定した値は全て存在しないとエラーとなるみたい
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector as mycon
import numbering
import CodeMasta
import logging


app = FastAPI()
app.include_router(numbering.router)
app.include_router(CodeMasta.router)

# CORSの設定　クロスオリジンのIP許可List
origins = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://192.168.0.10:8080",

]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
@app.get('/testinsert')
def indexa():
    cnx = None
    try:
        cnx = mycon.connect(
            user='admin',  # ユーザー名
            password='0000',  # パスワード
            host='192.168.0.20'  # ホスト名(IPアドレス）
        )
        if cnx.is_connected:
            print("Connected!")
        cursor = cnx.cursor()
        sql = '''
                INSERT INTO a_system.m_staff
                (scode, sname1, sname2)
                VALUES(%s, %s, %s);
        '''
        data = [
            ("0003", "ごんざぶろう", "淳之介"),
            ("0004", "かものはし", "芽依美"),
            ("0005", "まいまい", "テンペスト"),
        ]
        cursor.executemany(sql, data)
        cnx.commit()
        return {"message": (f"{cursor.rowcount} records inserted.")}
        cursor.close()
    except Exception as e:
        print(f"Error Occurred: {e}")
    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()


@app.get("/select")
def index():
    cnx = None
    try:
        cnx = mycon.connect(
            user='admin',  # ユーザー名
            password='0000',  # パスワード
            host='192.168.0.20',  # ホスト名(IPアドレス）
            database='a_system'  # データベース名
        )

        cursor = cnx.cursor()

        sql = ('''
            SELECT scode, sname1, sname2
            FROM a_system.m_staff
            WHERE scode = %s
            OR scode = %s;
        ''')

        param = ('0000', '0002',)  # カンマをつけると文字列型　つけないとタプルになる

        cursor.execute(sql, param)

        # for (scode, sname1, sname2) in cursor:
        #    print(f"{scode} {sname1} {sname2}")

        data = []
        for i in cursor:
            print(i)
            data.append(i)

        cursor.close()
        return data

    except Exception as e:
        print(f"Error Occurred: {e}")

    finally:
        if cnx is not None and cnx.is_connected():
            cnx.close()
"""
