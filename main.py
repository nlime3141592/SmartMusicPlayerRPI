from flask import Flask

import db
import webserver
import router

def main():
    try:
        db.init()
        webserver.init()
        webserver.get_blueprint().register_blueprint(router.init())
        webserver.run()
    except Exception as ex:
        print(f"Flask 서버 실행 중 오류 발생: {ex}")
    finally:
        webserver.final()
        db.final()

if __name__ == "__main__":
    main()