#!/usr/bin/env python
# coding:utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/23/18

import random


def gcd(a, b):
    """
    gcd двух чисел
    :param a:
    :param b:
    :return: gcd(a, b)
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def relativePrime(*args):
    """
    Проверка на взаимопростоту
    :param args: числа (произовольное кол-во)
    :return: True - если все взаимопростые, False - в другом случае
    """
    for i in args:
        assert i > 0, 'Числа должны быть > 0'
    success = True
    for i in args:
        for j in args:
            if i != j and gcd(i, j) != 1:
                success = False
                break
    return success


def FermatTest(n, test=50):
    success = True
    for t in range(test):
        a = random.randint(1, 10000)
        while not relativePrime(a, n):
            a = random.randint(1, 10000)
        if not pow(a, n-1, n) == 1:
            success = False
            break
    return success


if __name__ == '__main__':
    # test
    for i in range(1, 250):
        print(f'{i}, is prime - {FermatTest(i)}')
