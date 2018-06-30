# Rotate Image
# matrix is n x n, rotate it clockwise, do it in place
class Solution(object):
    def rotate(self, matrix):
        if not any(matrix):
            return matrix

        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                self.rotate_single(matrix, i, j)

    def rotate_single(self, matrix, i, j):
        n = len(matrix)
        # top to right
        right = matrix[j][n-i-1]
        matrix[j][n-i-1] = matrix[i][j]
        # right to bottom
        bottom = matrix[n-i-1][n-j-1]
        matrix[n-i-1][n-j-1] = right
        # bottom to left
        left = matrix[n-j-1][i]
        matrix[n-j-1][i] = bottom
        # left to top
        matrix[i][j] = left
# smart solution: reverse the matrix horizontally,
# then flip it symmetrically
