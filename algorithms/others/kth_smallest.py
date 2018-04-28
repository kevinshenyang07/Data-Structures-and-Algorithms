# Kth Smallest Element in a Sorted Matrix
# matrix is n x n, assume matrix and k is valid

#
# binary search approach
def kth_smallest_bisect(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[n-1][n-1]
    while lo < hi:
        mid = lo + (hi - lo) / 2
        cnt = sum([binary_search(row, mid) for row in matrix])
        if cnt < k:
            lo = mid + 1
        else:
            hi = mid
    return lo
# O(nlogn * log(max - min)) time, O(1) space
# since log(max - min) is up to 32 for int, can be considered as O(nlogn) time

# count of numbers <= target
# => index of first number > target
def binary_search(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) / 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return l


#
# search from lower-left / upper-right corner: similar to Search a 2D Matrix II
def kth_smallest(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[n-1][n-1]
    while lo < hi:
        mid = lo + (hi - lo) / 2
        cnt = count_nubmers_no_greater_than_mid(matrix, mid)
        if cnt < k:
            lo = mid + 1  # kth element should be in range (mid+1, hi]
        else:
            hi = mid
    return lo
# O(nlog(max - min)) time, O(1) space
# since log(max - min) is up to 32 for int, can be considered as O(n) time

# count of numbers <= target
def count_nubmers_no_greater_than_mid(matrix, target):
    n = len(matrix)
    i, j = n - 1, 0  # from the left-lower corner:
    cnt = 0
    while i >= 0 and j < n:
        if matrix[i][j] <= target:
            # add count of numbers above and move right
            cnt += i + 1
            j += 1
        else:
            i -= 1
    return cnt
