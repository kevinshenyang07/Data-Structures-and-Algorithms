# Spiral Matrix
class Solution(object):
    def spiralOrder(self, matrix):
        if not any(matrix):
            return []

        # mark the boundary lines
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        while True:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            if top > bottom or left > right:
                break

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top > bottom or left > right:
                break

            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom or left > right:
                break

            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if top > bottom or left > right:
                break

        return result


# Spiral Matrix II
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]

        x = y = 0
        dx, dy = 0, 1

        for i in range(1, n * n + 1):
            matrix[x][y] = i

            # turns right if next position is visited
            if matrix[(x + dx) % n][(y + dy) % n]:
                dx, dy = dy, -dx

            x += dx
            y += dy

        return matrix
