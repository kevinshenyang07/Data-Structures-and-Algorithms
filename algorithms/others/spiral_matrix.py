# Spiral Matrix
class Solution(object):
    def spiral_order(self, matrix):
        if not any(matrix):
            return []

        # mark the boundary lines
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        while True:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            if left > right or top > bottom: break;

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if left > right or top > bottom: break;

            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            if left > right or top > bottom: break;

            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right or top > bottom: break;

        return result
