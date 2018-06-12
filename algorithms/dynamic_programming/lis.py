# -*- coding:utf-8 -*-
from __future__ import print_function


# Longest Increasing Subsequence
def naive_lis(seq):
    '''
    state transition function:

    c[i] = max(c[j]) + 1 (0 < j < i) if arr[j] < arr[i]
         = 1                     if arr[j] > arr[i]
    '''
    n = len(seq)
    if n == 0:
        return 0
    else:
        B = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if seq[i] > seq[j]:  # and B[i] < B[j] + 1:
                    B[i] = B[j] + 1
        return max(B), B


def lis(seq):
    '''
    B[i] the smallest possible number at the end of a subsequence of length i+1
    use binary search instead of traversal
    '''
    left = right = mid = res = 1
    n = len(seq)
    B = [0] * n
    B[0] = seq[0]
    for i in range(1, n):
        left = 0
        right = res
        while left <= right:
            mid = (left + right) // 2
            if B[mid] < seq[i]:
                left = mid + 1
            else:
                right = mid - 1
        B[left] = seq[i]
        if left > res:
            res += 1
        print(B)
    return res, B


if __name__ == '__main__':
    seq = [2, 1, 5, 3, 6, 4, 8, 9, 7]

    res1 = naive_lis(seq)
    res2 = lis(seq)
    # print(res1)
    print(res2)
