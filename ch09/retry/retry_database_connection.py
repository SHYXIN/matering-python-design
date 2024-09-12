import logging
import random
import time


logging.basicConfig(level=logging.DEBUG)

def retry(attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(attempts):
                try:
                    logging.info("Retry happening")
                    return func(*args, **kwargs)
                except Exception as e:
                    time.sleep(1)
                    logging.debug(e)
            return "Failure after all attemps"
        return wrapper

    return decorator



@retry(attempts=3)
def connect_to_database():
    if random.randint(0, 1):
        raise Exception("Temporary Database Error")
    return "Connected to Database"

# 手动应用装饰器
# connect_to_database = retry(attempts=3)(connect_to_database)

# 调用函数，传入参数
# result = connect_to_database("database_url", 5)


if __name__ == "__main__":
    for i in range(1, 6):
        logging.info(f"Connection attempt #{i}")
        print(f"--> {connect_to_database()}")
