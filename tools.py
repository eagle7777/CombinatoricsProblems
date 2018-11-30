#!/usr/bin/env python
# coding:utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/24/18

import time


def benchmark(f):
    """
    Декоратор @benchmark для вычисления времени работы функции f
    """
    def _benchmark(*args, **kw):
        t = time.clock()
        rez = f(*args, **kw)
        t = time.clock() - t
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez
    return _benchmark


def memo(f):
    """
    Декортор @memo для кэширования функции f
    """
    m = {}

    def _memo(*args):
        if args in m:
            return m[args]
        else:
            res = f(*args)
            m[args] = res
            return res
    return _memo
