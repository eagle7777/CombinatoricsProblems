#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/29/18


"""
Задача о разрезании отрезка
"""

import sys
from tools import memo


@memo
def CutRod(p: list, n: int) -> int:
    """
    по заданным отрезку и длину стержня находит максимальную прибыль
    :param p: список стоимости стержней разных длин (индекс - длина, элемент - стоимость)
    :param n: длина стержня
    :return:
    """
    if n == 0:
        return 0
    q = - sys.maxsize
    for i in range(n):
        q = max(q, p[i] + CutRod(p, n - i - 1))  # разбиваем задачи на подзадачи (рекурсивно)
    return q


if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(CutRod(p, len(p)))
