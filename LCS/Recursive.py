#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/10/18
from tools import memo
import time

# task 1
@memo
def recursive(a, i, j):
    if i == j:
        return 1, (a[i], )
    _pre_count, _pre_seq = recursive(a, i-1, j)
    if a[i] >= _pre_seq[-1]:
        return _pre_count + 1, _pre_seq + (a[i], )
    else:
        max_count = 1
        max_seq = (a[i],)
        for k in range(j, i):
            tmp_count, tmp_seq = recursive(a, i-1, k)
            if tmp_count+1 > max_count and a[i] >= tmp_seq[-1]:
                max_count = tmp_count + 1
                max_seq = tmp_seq + (a[i], )
        for k in range(i):
            tmp_count, tmp_seq = recursive(a, k, 0)
            if tmp_count+1 > max_count and a[i] >= tmp_seq[-1]:
                max_count = tmp_count + 1
                max_seq = tmp_seq + (a[i], )
        return (max_count, max_seq) if max_count > _pre_count else (_pre_count, _pre_seq)


if __name__ == '__main__':
    start = time.time()
    b = '12314324525698'
    ans = recursive(b, len(b)-1, 0)
    end = time.time()
    print(ans[0], ''.join(ans[1]))
    print('time elapsed: ', end - start)