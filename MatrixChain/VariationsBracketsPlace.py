#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/1/18


from tools import memo


@memo
def P(n):
    """
    Возвращает по заданному кол-ву матриц колв-во способов расставить скобки в цепи
    :param n: кол-во матриц (длина цепи)
    :return: кол-во спосбов
    """
    if n == 1:
        return 1
    return sum([P(k) * P(n - k) for k in range(1, n)])


if __name__ == '__main__':
    print(P(6))
