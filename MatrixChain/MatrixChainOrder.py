#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/1/18

import sys
from MatrixChain import Matrix
from tools import benchmark, memo


@benchmark
def MatrixChainOrder(p: list) -> tuple:
    """
    для заданной цепочки матриц A[i] возвращает минимальное кол-во операций
    матрица A[i] имеетразмер p[i-1] x p[i]  1<=i<=n
    стоимость - кол-во умножений скаляров
    :param p: список длин матриц (длина списка на 1 больше чем кол-во матриц) высоту матрицы задает длина предыдущей
    :return:
    """
    n = len(p) - 1
    m = Matrix.Matrix.zeros(n, n)  # вспомогательная таблица для хранения стоимости (решений подзадач)
    s = Matrix.Matrix.zeros(n, n)  # таблица индексов для которых достигается оптимальная стоимость
    for i in range(n):
        m[i][i] = 0
    for l in range(1, n):
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = sys.maxsize + 1
            for k in range(j-1):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def PrintOptimalParents(s, i, j):
    if i == j:
        print(f'A[{i}]', end='')
    else:
        PrintOptimalParents(s, i, s[i, j])
        PrintOptimalParents(s, s[i, j] + 1, j)


if __name__ == '__main__':
    _ = MatrixChainOrder([30, 35, 15, 5, 10,  20, 25])
    print(_[0])
    print(_[1])
    print(_[0][2][5])
    print()
    PrintOptimalParents(list(_[1]), 2, 5)
