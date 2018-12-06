#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/6/18

from tools import benchmark


@benchmark
def GreedyActivivtySelector(s, f):
    """
    жадный алгоритм
    :param s: список начал процессов
    :param f: список концов процессов
    :return: макс множество процессов
    """
    n = len(s)
    A = [(s[0], f[0])]
    k = 1
    for m in range(2, n):
        if s[m] >= f[k]:
            A += [(s[m], f[m])]
            k = m
    return A


if __name__ == '__main__':
    # test
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print(GreedyActivivtySelector(s, f))
