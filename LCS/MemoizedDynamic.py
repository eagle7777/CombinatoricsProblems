#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/10/18

from tools import benchmark


# task 5
@benchmark
def dynamic(a, b):
    m = len(a)
    n = len(b)
    val = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if a[i] == b[j]:
                val[i][j] = val[i-1][j-1] + 1
            else:
                val[i][j] = max(val[i-1][j], val[i][j-1])
    return val


if __name__ == '__main__':
    a = '100234'
    b = '0124'
    ans = dynamic(a, b)
    print(max(map(max, ans)))
