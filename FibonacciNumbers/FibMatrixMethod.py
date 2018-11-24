#!/usr/bin/env python
# coding:utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/24/18

import numpy as np
import time
from tools import benchmark

P = np.array([[0, 1], [1, 1]])
V = np.array([0, 1])  # вектор (Fib[0], Fib[1])


@benchmark
def fib(n):
    """
    Матричный метод нахождени числа Фибоначчи
    работает за O(log(N))
    V * P^n = [Fib[n-1], Fib[n]]
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return abs(list(V.dot(np.linalg.matrix_power(P, n)))[1])


if __name__ == '__main__':
    n = 0
    while True:
        n += 1
        t_start = time.time()
        print(f'fib({n}) = {fib(n)}')
        t_end = time.time()
        if t_end - t_start >= 60:
            print(f'\n---- n = {n} ----\n')
            break
