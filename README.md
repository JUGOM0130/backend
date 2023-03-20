導入
pip install fastapi uvicorn
requirements.txtから導入でもOK

サーバー起動コマンド
uvicorn main:app --reload
    解説：main.pyのFastAPIインスタンスを指定 app=FastAPI()


2023/03/20
python　コマンドから起動でもOK
引数にWIN→会社用
引数にPRO→本番用
引数なし→検証（Mac用）