#!/usr/bin/env python
# coding:utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/24/18

import random
import time
from PrimalityTest import CarmichaelNumbers
from tools import benchmark


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


def prepare(n):
    """

    Представить число n в виде 2**s*t, t = 2*k+1 (нечетно)

    :param n:
    :return: (s, t)
    """
    s = 0
    while not n % 2:
        n /= 2
        s += 1
    return s, n


def moduloPow(a, b, m):
    """

    Возведение в степень по модулю
    a**b (mod m)

    :param a:
    :param b:
    :param m:
    :return: a**b (mod m)
    """
    return pow(a, b, m)


def check(a, s, t, n):
    """

    Вспомогательная функция проверки на простоту для отдельного свидетеля простоты a

    :param a:
    :param s:
    :param t:
    :param n:
    :return: True - простое , False - составное
    """
    x = moduloPow(a, t, n)
    if x == 1:
        return True
    for i in range(s - 1):
        if x == n - 1:
            return True
        x = moduloPow(x, 2, n)
    return x == n - 1


@benchmark
def MillerRabin(n, k=50):
    """

    Тест на простоту Миллера-Рабина

    :param n: число для проверки
    :param k: кол-во тестов
    :return: True - вероятно простое, False - составное
    """
    if n in [1, 2, 3]:
        return True
    if not n & 1:  # проверка на парность
        return False
    if CarmichaelNumbers.CarmichaelCheck(n):  # проверка на число Кармайкла
        return False
    s, t = prepare(n-1)
    for i in range(k):
        a = random.randrange(2, n-1)
        if not check(a, s, int(t), n):
            return False
    return True


if __name__ == '__main__':
    # # test

    n = 2000
    for i in range(1, n):
        print(f'{i}, is simple - {MillerRabin(i)}\n')
