#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/1/18

import sys
from MatrixChain import Matrix
from tools import benchmark, memo


@benchmark
def MatrixChainOrder(p):
    n = len(p) - 1
    m = Matrix.Matrix.zeros(n, n)
    s = Matrix.Matrix.zeros(n, n)
    for i in range(n):
        m[i][i] = 0
    for l in range(1, n):
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = sys.maxsize + 1
            for k in range(j-1):
                q = m[i][k] + m[k+1][j] + p[i-1] + p[k] + p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s