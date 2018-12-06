#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/6/18


def RecursiveActiveSelector(start, finish, k, n):
    """
    рекурсивный алгоритм
    :param start: список начал процессов
    :param finish: список конец процессов
    :param k: стартовое время
    :param n: конечное время
    :return: макс множество процессов
    """
    m = k + 1
    while m <= n and start[m] < finish[k]:
        m += 1
    if m <= n:
        return [(start[m], finish[m])] + RecursiveActiveSelector(start, finish, m, n)
    else:
        return []


if __name__ == '__main__':
    # test
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print(RecursiveActiveSelector(s, f, 1, 5))