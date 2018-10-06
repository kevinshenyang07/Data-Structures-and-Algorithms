from binary_indexed_tree import BIT, BIT2D

# Range Sum Query - Mutable
# find the sum of the elements between indices i and j (i ≤ j), inclusive.
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.tree = BIT(len(nums))
        # calculate initial sums
        for i, num in enumerate(nums):
            self.tree.accumulate(i, num)

    def update(self, i, val):
        # calculuate diff and update orignal array first
        diff = val - self.nums[i]
        self.nums[i] = val
        self.tree.accumulate(i, diff)

    def sumRange(self, i, j):
        return self.tree.query(j) - self.tree.query(i - 1)
# O(logn) time, O(n) space


# Range Sum Query 2D - Mutable
class NumMatrix(object):
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.tree = BIT2D(m, n)
        # calculate initial sums
        for i in range(m):
            for j in range(n):
                self.tree.accumulate(i, j, matrix[i][j])

    def update(self, i, j, val):
        # calculuate diff and update orignal array first
        diff = val - self.matrix[i][j]
        self.matrix[i][j] = val
        self.tree.accumulate(i, j, diff)

    def sumRegion(self, i1, j1, i2, j2):
        area_upper_left = self.tree.query(i1 - 1, j1 - 1)
        area_upper = self.tree.query(i1 - 1, j2)
        area_left = self.tree.query(i2, j1- 1)
        area_total = self.tree.query(i2, j2)
        return area_total - area_upper - area_left + area_upper_left
# O(logm * logn) time, O(m * n) space
