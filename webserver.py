from flask import Flask

s_flask = None

def init():
    global s_flask

    try:
        s_flask = Flask(__name__)
        print("Flask 애플리케이션이 성공적으로 초기화되었습니다.")
    except Exception as ex:
        print(f"Flask 초기화 중 오류 발생: {ex}")
        raise

def final():
    global s_flask

    if s_flask:
        print("Flask 애플리케이션 종료")
    else:
        print("Flask 애플리케이션이 초기화되지 않았습니다.")

def run():
    global s_flask

    if s_flask is None:
        print("Flask 애플리케이션이 초기화되지 않았습니다.")
        return

    try:
        s_flask.run(
            host="0.0.0.0",
            debug=True,
            port=5000,
            use_reloader=True)
    except Exception as ex:
        print(f"Flask 서버 실행 중 오류 발생: {ex}")

def get_blueprint():
    global s_flask

    return s_flask