#!/usr/bin/env python
# coding:utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/24/18

import time
from tools import benchmark, memo


@memo
@benchmark
def fib(n):
    """
    Нахождение n числа Фибоначи
    :param n: номер
    :return: искомое число
    """
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


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
