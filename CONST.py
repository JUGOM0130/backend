import sys
import logging

# デフォルト設定
logging.basicConfig(level=logging.DEBUG)
CONST = {
    'user': 'admin',
    'pw': '0000',
    'host': '192.168.0.20',
    'db': 'a_system'
}

if len(sys.argv) > 0:
    # 本番環境用設定
    if sys.argv[0] == "PRO":
        print("本番環境運用")
        # ログレベル設定 リリース時はINFO以上に設定する
        logging.basicConfig(level=logging.DEBUG)

        # 定数設定
        CONST = {
            'user': 'admin',
            'pw': '0000',
            'host': '192.168.0.20',
            'db': 'a_system'
        }
    # 会社Windows
    elif sys.argv[0] == "WIN":
        print("Win環境運用")
        # ログレベル設定 リリース時はINFO以上に設定する
        logging.basicConfig(level=logging.DEBUG)

        # 定数設定
        CONST = {
            'user': 'admin',
            'pw': '0000',
            'host': '192.168.0.20',
            'db': 'a_system'
        }
    # 検証環境用
    else:
        print("検証環境運用")
        # ログレベル設定 リリース時はINFO以上に設定する
        logging.basicConfig(level=logging.DEBUG)

        # 定数設定
        CONST = {
            'user': 'admin',
            'pw': '0000',
            'host': '192.168.0.20',
            'db': 'a_system'
        }
