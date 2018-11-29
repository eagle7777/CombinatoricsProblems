#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/29/18


import random


def cutRod(p, n, price=0):
    """

    :param p:
    :param n:
    :param price:
    :return:
    """
    val = [None for i in range(n+1)]
    val[0] = 0

    for i in range(1, n+1):
        max_val = -1
        for j in range(i):
            max_val = max(max_val, p[j] + val[i-j-1])
        val[i] = max_val
    return val[n]


if __name__ == '__main__':
    size = random.randrange(40)
    s = [random.randrange(40) for i in range(size)]
    print(s)
    print(cutRod(s, 10))
