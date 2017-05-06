"""
    multiprocess モジュールを使った実装サンプル.

    リファレンス：
        https://docs.python.jp/3/library/multiprocessing.html
"""
import time
import os

# Process クラス
###################
from multiprocessing import Process

def f1(name):
    print("Hello", name)
    print("Sleeping... 3s")
    time.sleep(3)
    print("Good morning", name)

# if __name__ == "__main__":
#     p = Process(target=f1, args=("Bob",))
#     p.start()
#     print("Process started.")
#     p.join()
#     print("Process joined.")


# Process 間でのデータのやりとり
###################

# Queue を使う場合
from multiprocessing import Queue

def f2(q):
    time.sleep(3)
    q.put([42, None, "Hello"])

# if __name__ == "__main__":
#     q = Queue()
#     p = Process(target=f2, args=(q,))
#     p.start()
#     # q.get() できるまで待つ.
#     print(q.get())
#     p.join()


# Pipe を使う場合
from multiprocessing import Pipe

def f3(conn):
    time.sleep(3)
    conn.send([42, None, "Hello"])
    conn.close()
    # conn.send([42, None, "Hello"])  # OSError: handle is closed

# if __name__ == "__main__":
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f3, args=(child_conn,))
#     p.start()
#     # parent_conn.recv() できるまで待つ.
#     print(parent_conn.recv())
#     p.join()


# Lock を用いたプロセス間の同期
###################
from multiprocessing import Lock

def f4(lock, i):
    lock.acquire()
    try:
        print('Hello', i)
    finally:
        lock.release()

# if __name__ == "__main__":
#     lock = Lock()
#     for num in range(10):
#         Process(target=f4, args=(lock, num)).start()
#     # print("aaa")


# 状態の共有
###################

# 共有メモリ（Shared memory）の利用
from multiprocessing import Value, Array

def f5(n, a):
    n.value = 3.1415926
    for i in range(len(a)):
        a[i] *= -1

# if __name__ == "__main__":
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))
#     p = Process(target=f5, args=(num, arr))
#     p.start()
#     p.join()
#     print(num.value)
#     print(arr[:])

# マネージャー（Manager）の利用
from multiprocessing import Manager

def f6(d, l):
    d[1] = '1'
    d["2"] = 2
    d[0.25] = None
    l.reverse()

# if __name__ == "__main__":
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list(range(10))
#         p = Process(target=f6, args=(d,l))
#         p.start()
#         p.join()
#         print(d)
#         print(l)


# ワーカープロセスのプール（Poolクラス）
###################
from multiprocessing import Pool, TimeoutError

def f7(x):
    return x*x

if __name__ == "__main__":
    # Start 4 worker processes.
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f7, range(10)))

        # print same numbers in arbitrary order.
        for i in pool.imap_unordered(f7, range(10)):
            print(i)

        # Evaluate "f7(20)" asynchronously.
        res = pool.apply_async(f7, (20,))  # runs in *only* one process.
        print(res.get(timeout=1))         # print "400"

        # launching multiple evaluations asynchronously *may* use more processes.
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(10)]
        results = [res.get(timeout=1) for res in multiple_results]
        print(results)
        print(set(results), len(set(results)))

        # Timeout error.
        res = pool.apply_async(time.sleep, (10,))
        try:
            res.get(timeout=1)
        except TimeoutError as e:
            print("Timeout.....!!!", e)

        # Work fine.
        print("With句の中ではProcessは生きています.")

    print("With句から出るとProcessは利用できなくなります.")



