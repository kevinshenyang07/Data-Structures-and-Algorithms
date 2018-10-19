from collections import deque

# Toeplitz Matrix
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
# Assume the matrix has at least one row and one column.
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False

        return True

# Followup:
# what if the matrix is so big that we can only load a partial row into memory each time?
# Approach:
# essentially we are trying to compare if matrix[i - 1][:-1] == matrix[i][1:] all the time
# so we just need to keep track of the hash of matrix[i][:-1] and matrix[i][1:] between two lines
