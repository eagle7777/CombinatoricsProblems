#!/usr/bin/env python
# coding:utf-8
# Author: Valentyn Kofanov (knu)
# source: 
# Created: 11/23/18

import random


def FermatTest(n, test=1):
    success = True
    for t in range(test):
        a = random.randint(1, n-1)
        while a % n != 0:
            a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            success = False
            break
    return success


if __name__ == '__main__':
    print(FermatTest(26))