"""
    multiprocess モジュールを使った実装サンプル.

    リファレンス：
        https://docs.python.jp/3/library/multiprocessing.html
"""
import time
import os
import sys

# Process クラス
###################
from multiprocessing import Process

def f1(name):
    print("Hello", name)
    print("Sleeping... 3s")
    time.sleep(3)
    print("Good morning", name)

# if __name__ == "__main__":
#     # Processを作成します
#     p = Process(target=f1, args=("Bob",))
#     # 開始します
#     p.start()
#     print("Process started.")
#     # サブプロセス終了まで待ちます
#     p.join()
#     print("Process joined.")


# Process 間でのデータのやりとり
###################

# Queue を使う場合
from multiprocessing import Queue

def f2(q):
    time.sleep(3)
    # 3秒後に、キューに値を渡します.
    q.put([42, None, "Hello"])

# if __name__ == "__main__":
#     # スレッド間でやり取りするためのキューを作成します.
#     q = Queue()
#     # キューを引数に渡して、サブプロセスを作成します.
#     p = Process(target=f2, args=(q,))
#     # サブプロセスを開始します.
#     p.start()
#     # q.get()できるまで待ちます.
#     print(q.get())
#     # サブプロセス完了を待ちます.
#     p.join()


# Pipe を使う場合
from multiprocessing import Pipe

def f3(conn):
    time.sleep(3)
    # パイプにデータを送信します.
    conn.send({ "age" : 30, "name" : "Yohei" })
    # パイプをクローズします.
    conn.close()
    # conn.send([42, None, "Hello"])  # OSError: handle is closed

# if __name__ == "__main__":
#     # Pipeを生成します（デフォルトでは双方向にやり取りできるパイプ）
#     # 双方向にやり取りできますが、両端で自由に読み書きしているとデータが壊れる可能性があるので、
#     # 基本的にはどちらかを書き込み専用、どちらかを読み込み専用に扱います.
#     parent_conn, child_conn = Pipe()
#     # Pipeの片方の端を、サブプロセスに渡します.
#     p = Process(target=f3, args=(child_conn,))
#     # サブプロセスを開始します.
#     p.start()
#     # Pipeから値が取得できるまで待ちます.
#     print(parent_conn.recv())
#     # サブプロセスの終了を待ちます.
#     p.join()



# Lock を用いたプロセス間の同期
###################
from multiprocessing import Lock

def f4(lock, i):
    # ロックを取得します.
    lock.acquire()
    # ロック中は、他のプロセスやスレッドがロックを取得できません（ロックが解放されるまで待つ）
    try:
        print('Hello', i)
    finally:
        # ロックを解放します.
        lock.release()

# if __name__ == "__main__":
#     # ロックを作成します.
#     lock = Lock()
#     for num in range(10):
#         Process(target=f4, args=(lock, num)).start()


# 状態の共有
###################

# 共有メモリ（Shared memory）の利用
from multiprocessing import Value, Array

def f5(n, a):
    n.value = 3.1415926
    for i in range(len(a)):
        a[i] *= -1

# if __name__ == "__main__":
#     # 共有メモリ（Value）を作成します.
#     num = Value('d', 0.0)
#     # 共有メモリ（Array）を作成します.
#     arr = Array('i', range(10))
#     # サブプロセスを作り、実行します.
#     p = Process(target=f5, args=(num, arr))
#     p.start()
#     p.join()
#     # 共有メモリ（Value）から値を取り出します
#     print(num.value)
#     # 共有メモリ（Array）から値を取り出します
#     print(arr[:])


# マネージャー（Manager）の利用
from multiprocessing import Manager

def f6(d, l):
    # 辞書型に値を詰め込みます.
    d[1] = '1'
    d["2"] = 2
    d[0.25] = None
    # 配列を操作します（ここでは逆順に）.
    l.reverse()

if __name__ == "__main__":
    # マネージャーを生成します.
    with Manager() as manager:
        # マネージャーから辞書型を生成します.
        d = manager.dict()
        # マネージャーから配列を生成します.
        l = manager.list(range(10))
        # サブプロセスを作り実行します.
        p = Process(target=f6, args=(d,l))
        p.start()
        p.join()
        # 辞書からデータを取り出します.
        print(d)
        # 配列からデータを取り出します.
        print(l)


# ワーカープロセスのプール（Poolクラス）
###################
from multiprocessing import Pool, TimeoutError

def f7(x):
    return x*x

if __name__ == "__main__":
    # 4つのプロセスを開始します.
    with Pool(processes=4) as pool:

        # 0〜9の10個の値を、4つのプロセスで処理します.
        print(pool.map(f7, range(10)))
        # print: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

        # ひとつ上と似ていますが、プロセスの実行順が不定になります.
        for i in pool.imap_unordered(f7, range(10)):
            print(i)
            # print: 0, 1, 4, 16, 9, 25, 36, 49, 64, 81

        # "f7(20)"という処理を非同期に実行します（利用するプロセスは1つのみ）
        res = pool.apply_async(f7, (20,))
        # 処理結果が返ってくるまで、最大1秒間待機します
        print(res.get(timeout=1))
        # print: 400

        # 上記の仕組みを連続して呼ぶと、複数のプロセスで処理を行うことができます.
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(10)]
        results = [res.get(timeout=1) for res in multiple_results]
        # 10個出力されます
        print(results)
        # print : [37604, 37607, 37606, 37605, 37604, 37607, 37606, 37605, 37604, 37607]

        # ただしユニークにすると4つのみ（=プールしたプロセス数）であることがわかります
        print(set(results), len(set(results)))
        # {37604, 37605, 37606, 37607} 4

        # タイムアウトが発生する場合のサンプルです
        res = pool.apply_async(time.sleep, (10,))
        try:
            res.get(timeout=1)
        except TimeoutError as e:
            print("Timeout.....!!!", e)
