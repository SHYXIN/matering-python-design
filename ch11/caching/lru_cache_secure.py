from functools import lru_cache
import threading
import time

@lru_cache(maxsize=128)
def expensive_computation(n):
    # 模拟一个耗时的计算
    time.sleep(2)
    return n * n

# 用于多线程调用函数
def worker(n):
    print(f"Thread {n} result: {expensive_computation(n)}")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(2,))
    threads.append(t)
    t.start()

# 等待所有线程结束
for t in threads:
    t.join()
