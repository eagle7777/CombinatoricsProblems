#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/7/18


def get_subset(s, f, i, j):
    if i == 0:
        start = 0
    else:
        start = f[i - 1]
    if j == len(s):
        finish = 1 << 20
    else:
        finish = s[j]
    res = [(s[k], f[k]) for k in range(len(s)) if s[k] > start and f[k] < finish]
    return res


def ASPDynamic(s, f, v):
    """
    Динамический алгоритм
    :param s: список начал
    :param f: список концов
    :param v: список цен
    :return:
    """
    l = len(s)
    vals = [[None for _ in range(l)] for _ in range(l)]
    indxs = [[None for _ in range(l)] for _ in range(l)]
    for a in range(l):
        vals[a][a] = 0
    for c1 in range(1, len(vals)):
        for c2 in range(c1, len(vals)):
            i, j = c2 - c1, c2
            mx = 0
            kx = -1
            for k in range(i + 1, j):
                if get_subset(s, f, i, j):
                    tmp = vals[i][k] + vals[k][j] + v[k]
                    if tmp > mx:
                        mx = tmp
                        kx = k
            vals[i][j] = mx
            indxs[i][j] = kx
    return vals, indxs


def get_res(indxs, i, j):
    if indxs[i][j] == -1 or indxs[i][j] is None:
        return ''
    else:
        k = indxs[i][j]
        return get_res(indxs, i, k) + ' ' + str(k) + ' ' + get_res(indxs, k, j)


if __name__ == '__main__':
    from random import randrange as rand
    # s = [1, 3, 0, 5, 3, 5]
    # f = [4, 5, 6, 7, 9, 9]
    # v = [rand(1, 30) for i in range(len(s))]
    s = [0, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6]
    f = [2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8]
    v = [3, 4, 4, 4, 4, 2, 4, 4, 4, 4, 3]
    print(v, end='\n\n')
    r1, r2 = ASPDynamic(s, f, v)
    print(get_res(r2, 0, len(s)-1))
