#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/29/18


"""
Задача о разрезании отрезка
"""

import sys
from tools import memo, benchmark


class MyList(list):
    """
    список со взятием хэша
    """
    def __hash__(self):
        return str.__hash__(str(self))


@benchmark
def CutRodRecursively(p: MyList, n: int) -> int:
    """
    по заданным отрезку и длину стержня находит максимальную прибыль
    :param p: список стоимости стержней разных длин (индекс - длина, элемент - стоимость)
    :param n: длина стержня
    :return:
    """
    if n == 0:
        return 0
    q = - sys.maxsize - 1
    for i in range(n):
        q = max(q, p[i] + CutRodRecursively(p, n - i - 1))  # разбиваем задачи на подзадачи (рекурсивно)
    return q


@memo
@benchmark
def CutRodDynamic(p: MyList, n: int) -> int:
    """
    по заданным отрезку и длине стержня находит максимальную прибыль
    :param p: список стоимости стержней разных длин (индекс - длина, элемент - стоимость)
    :param n: длина стержня
    :return:
    """
    if n == 0:
        return 0
    q = - sys.maxsize - 1
    for i in range(n):
        q = max(q, p[i] + CutRodDynamic(p, n - i - 1))  # разбиваем задачи на подзадачи (рекурсивно)
    return q


if __name__ == '__main__':
    # test
    p = MyList([1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    print(CutRodRecursively(p, len(p)))
    print(CutRodDynamic(p, len(p)))


