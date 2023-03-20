#!python3.11
# サーバー起動　uvicorn main:app --reload
# 400 Bad Request :　どこのIPから許可するかを設定で解決
# 422 Unprocessable Entity : 型が理解できないエラー（バリデーションを設けてあげる
# クラスに指定した値は全て存在しないとエラーとなるみたい
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector as mycon
import numbering
import CodeMasta
import Parts
import logging
import CodeTemplate
import Tree

app = FastAPI()
app.include_router(numbering.router)
app.include_router(CodeMasta.router)
app.include_router(CodeTemplate.router)
app.include_router(Parts.router)
app.include_router(Tree.router)

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
