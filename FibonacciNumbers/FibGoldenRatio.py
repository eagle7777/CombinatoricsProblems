#!/usr/bin/env python
# coding:utf-8
# Author: Valentyn Kofanov (knu)
#  Created: 11/24/18

import time
from tools import benchmark
import math


@benchmark
def fib(n):
    """
    Числа Фибоначчи через золотое сечение
    """
    return (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5)


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
