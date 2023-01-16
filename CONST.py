import logging

# ログレベル設定 リリース時はINFO以上に設定する
logging.basicConfig(level=logging.DEBUG)

# 定数設定
CONST = {
    'user': 'admin',
    'pw': '0000',
    'host': '192.168.0.20',
    'db': 'a_system'
}
