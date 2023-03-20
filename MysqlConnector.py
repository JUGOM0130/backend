import CONST
import mysql.connector as mycon

class Connector:

    def __init__(self) -> None:
        try:
            self.con = mycon.connect(
                        user=CONST.CONST['user'],  # ユーザー名
                        password=CONST.CONST['pw'],  # パスワード
                        host=CONST.CONST['host'],  # ホスト名(IPアドレス）
                        auth_plugin='mysql_native_password'
                        )
            self.con.ping(reconnect=True)#接続切れたときに再接続するか
            self.con.autocommit = False

            self.cur = self.con.cursor(dictionary=True)#データを辞書型で取得する

            # print(self.con.is_connected())
        except Exception as e:
            print(e)
            self.con.close()
            self.cur.close()

    def get_cursor(self):
        return self.cur
            
    def close(self) -> None:
        # cur閉じる
        self.cur.close()
        self.con.close()
        