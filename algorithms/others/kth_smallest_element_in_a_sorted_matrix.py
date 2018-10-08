# Kth Smallest Element in a Sorted Matrix
# given a n x n matrix where each of the rows and columns are sorted in ascending order
# find the kth smallest element in the matrix
# note that it is the kth smallest element in the sorted order, not the kth distinct element
# assume matrix and k is valid

# binary search approach
class SolutionV1(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while lo < hi:
            mid = lo + (hi - lo) / 2
            cnt = sum([self.binary_search(row, mid) for row in matrix])
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # count of numbers <= target
    # => index of first number > target
    def binary_search(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l
# O(nlogn * log(max - min)) time, O(1) space
# since log(max - min) is up to 32 for int, can be considered as O(nlogn) time


# search from lower-left / upper-right corner: similar to Search a 2D Matrix II
class SolutionV2(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        # use value range instead of index range
        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while lo + 1 < hi:
            mid = lo + (hi - lo) / 2
            cnt = self.count_nubmers(matrix, mid)
            if cnt < k:  # less than k elements <= mid
                lo = mid
            else:
                # do no return mid when cnt == k
                # since mid might not be a number in matrix
                hi = mid
        if self.count_numbers(matrix, lo) < k:
            return hi
        else:
            return lo

    # numbers <= target
    def count_nubmers(self, matrix, target):
        n = len(matrix)
        i, j = n - 1, 0  # from the left-lower corner:
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                # numbers in column j with row index <= i are smaller than target
                # count them in, then move right
                cnt += i + 1
                j += 1
            else:
                # numbers in row i with row index >= j are greater than target
                # nothing to be counted, move up
                i -= 1
        return cnt
# O(nlog(max - min)) time, O(1) space
# since log(max - min) is up to 32 for int, can be considered as O(n) time
