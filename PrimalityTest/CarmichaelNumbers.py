#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/23/18

import math


def sieveOfEratosthenes(n):
    """
    Проверка на простоту
    Решето Эратосфена
    :param n: число
    :return: True/False
    """
    succees = True
    for i in range(1, int(math.sqrt(n))+1):
        if not relativePrime(i, n):
            succees = False
            break
    return succees


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


def CarmichaelCheck(n):
    """
    проверка числа на число Кармайкла
    :param n: число
    :return: True/False
    """
    def _helpCheck(b, n):
        """тест Ферма"""
        return pow(b, n-1, n) == 1  # возведение в степень по модулю b**(n-1) = 1 (mod n)
    if sieveOfEratosthenes(n):
        return False
    success = True
    for i in range(1, n):
        if relativePrime(i, n) and not _helpCheck(i, n):
            success = False
            break
    return success


if __name__ == '__main__':
    # test
    print(CarmichaelCheck(561))
