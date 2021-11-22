# -*- coding:utf-8 -*-
import time
import threading as th


def isPrime(n):
    # 判断n是否为质数
    for i in range(2, int(n**(0.5))+1):  # [2, sqrt(n)]
        if n % i == 0:
            return False
    return True


def prime(Nth):
    # 找出第n个质数
    n_found = 0
    result = 0
    while n_found < Nth:
        result += 1
        n_found += isPrime(result)


def prime(Nth):
    n_found = 0
    result = 0
    while n_found< Nth:
        result += 1
        n_found += int(isPrime(result))
    return result


if __name__ == '__main__':
    start = 100000
    # singe process single thread
    t1 = time.time()
    print(prime(start), prime(start+1), prime(start+2), prime(start+3))
    print('Serial task took: ', time.time()-t1, 'seconds')

    # single process multi-threads
    t2 = time.time()
    jobs = [th.Thread(target=prime, args=(start,)),
            th.Thread(target=prime, args=(start+1,)),
            th.Thread(target=prime, args=(start+2,)),
            th.Thread(target=prime, args=(start+3,)),
            ]

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('multi-threads task took: ', time.time() - t2, ' seconds')
