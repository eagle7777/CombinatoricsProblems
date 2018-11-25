#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/25/18


import time
from tools import benchmark


def LCS(x: str, y:str):
    ...


# @benchmark
def c(i: int, j: int, x: str, y: str):
    if (i == 0 or j == 0) and x[i] == y[j]:
        return 1
    if i == 0 or j == 0:
        return 0
    if x[i] == y[j]:
        return c(i-1, j-1, x, y) + 1
    if x[i] != y[j]:
        return max(c(i-1, j, x, y), c(i, j-1, x, y))


if __name__ == '__main__':
    t_start = time.time()
    x = '1123456'
    y = '123'
    maxx = -1
    for i in range(len(x)):
         for j in range(len(y)):
             if c(i, j, x, y) > maxx:
                 maxx = c(i, j, x, y)
    print(maxx)
    t_end = time.time()
print(f'time elapsed : {t_end - t_start}')