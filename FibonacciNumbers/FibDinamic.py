#!/usr/bin/env python
# coding:utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/24/18

import time
from tools import benchmark


@benchmark
def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


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
