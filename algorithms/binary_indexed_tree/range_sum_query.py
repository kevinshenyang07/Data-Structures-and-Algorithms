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
        return self.tree.query(i2, j2) \
             - self.tree.query(i2, j1- 1) \
             - self.tree.query(i1 - 1, j2) \
             + self.tree.query(i1 - 1, j1 - 1)


# Range Sum Query 2D - Immutable
# assume #sumRegion args are valid
class NumMatrix(object):
    def __init__(self, matrix):
        if not any(matrix):
            self.sums = [[]]
        else:
            m, n = len(matrix), len(matrix[0])
            # extra row and col to simplify setup and query
            sums = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] - sums[i][j] + matrix[i][j]
            self.sums = sums

    def sumRegion(self, row1, col1, row2, col2):
        return self.sums[row2 + 1][col2 + 1] \
             - self.sums[row2 + 1][col1] \
             - self.sums[row1][col2 + 1] \
             + self.sums[row1][col1]
