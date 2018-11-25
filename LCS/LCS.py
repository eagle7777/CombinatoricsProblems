#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/25/18


from tools import benchmark


@benchmark
def LCS(x: str, y: str, showMatrix=False):
    m = findMatrix(x, y)
    if showMatrix:
        for row in m:
            print(row)
        print()
    return max([max(i) for i in m])


def c(i: int, j: int, x: str, y: str):
    if (i == 0 or j == 0) and x[i] == y[j]:
        return 1
    if i == 0 or j == 0:
        return 0
    if x[i] == y[j]:
        return c(i-1, j-1, x, y) + 1
    if x[i] != y[j]:
        return max(c(i-1, j, x, y), c(i, j-1, x, y))


def findMatrix(x: str, y: str):
    l1 = len(x)
    l2 = len(y)
    m = [[[] for _ in range(l2)] for _ in range(l1)]  # создаем пустую матрицу
    for i in range(l1):
        for j in range(l2):
            m[i][j] = c(i, j, x, y)
    return m


if __name__ == '__main__':
    x = '100234'
    y = '0124'
    print(LCS(x, y, showMatrix=True))
