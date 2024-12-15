import mariadb
import os
import re as regex

s_connection = None

def __get_db_info():
    info = {}
    file = None

    try:
        path = os.path.abspath("./db_info.txt")
        file = open(path, "r")

        for i in range(5):
            line = file.readline()

            if not line:
                raise ValueError("파일에 충분한 줄이 없습니다.")

            line = regex.sub(r"\s+", "", line)
            tokens = line.split(":")
            if len(tokens) != 2:
                raise ValueError(f"올바르지 않은 형식의 줄: {line}")

            info[tokens[0]] = tokens[1]

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except ValueError as ve:
        print(f"값 처리 중 오류 발생: {ve}")
    except Exception as ex:
        print(f"예기치 못한 오류 발생: {ex}")
    finally:
        if file:
            file.close()

    return info

def __get_db_connection():
    try:
        info = __get_db_info()

        connection = mariadb.connect(
            user=info["user"],
            password=info["password"],
            host=info["host"],
            port=int(info["port"]),
            database=info["database"]
        )

        return connection

    except mariadb.Error as ex:
        print(f"DB 연결 실패: {ex}")
        raise

def init():
    global s_connection

    s_connection = __get_db_connection()

def final():
    global s_connection

    if s_connection:
        try:
            s_connection.close()
            print("DB 연결 종료")
        except mariadb.Error as ex:
            print(f"DB 연결 종료 중 오류 발생: {ex}")
        finally:
            s_connection = None

def get_cursor():
    global s_connection

    return s_connection.cursor()

def commit():
    global s_connection

    s_connection.commit()