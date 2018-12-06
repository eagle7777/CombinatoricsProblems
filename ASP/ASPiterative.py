#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/7/18
from tools import benchmark


@benchmark
def ASPiterative(s, f):
    """
    итеративый алгоритм
    процессор задается кортежом (start time, finish time)
    :param s: список начал процессов
    :param f: список концов процессов
    :return: A - максимальное множество процессоров
    """
    A = []  # инициализируем множество
    n = len(f)
    i = 0
    A.append((s[i], f[i]))
    for j in range(n):
        if s[j] >= f[i]:
            A.append((s[j], f[j]))
            i = j
    return A


if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print(ASPiterative(s, f))
