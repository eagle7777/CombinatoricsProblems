#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/30/18

from tools import benchmark


@benchmark
def ExtendedBottomUpCutRod(p: list, n: int, price=0):
    """
    по заданным отрезку длине стержня и стоимости
    находит для каждой длины:
    максимальную прибыль
    и список раззрезов для заднной длины
    :param p: список стоимостей кусков стержня
    :param n: длина
    :param price: цена за разрез
    :return: список макс прибылей и список разрезов
    """
    res = [0] * (n + 1)
    seq = [[]] * (n + 1)
    for j in range(1, n + 1):
        q = 0
        cur_index = 0
        for i in range(j):
            if q < p[i] + res[j - i - 1] - price:
                q = p[i] + res[j - i - 1] - price
                cur_index = i
        seq[j] = seq[j - cur_index - 1] + [cur_index]
        res[j] = q
    return res, seq


if __name__ == '__main__':
    # test
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(ExtendedBottomUpCutRod(p, len(p)))
