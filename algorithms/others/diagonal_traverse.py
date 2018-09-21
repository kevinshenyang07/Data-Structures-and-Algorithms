# naive diagonal traverse (does not change direction when traversing)
# returns list of rows
# by observing indices of each row, one can find i + j == row_idx
def diagonal_order(matrix):
    if not any(matrix): return []

    m, n = len(matrix), len(matrix[0])
    visited = [[] for _ in range(m + n - 1)]

    for i in range(m):
        for j in range(n):
            visited[i + j].append(matrix[i][j])

    return visited

# Diagonal Traverse
# diagonal -> anti-diagonal -> diagonal ...
# returns a list of numbers
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not any(matrix):
            return []

        m, n = len(matrix), len(matrix[0])
        visited = [[] for _ in range(m + n + 1)]

        for i in range(m):
            for j in range(n):
                visited[i + j].append(matrix[i][j])

        output = []
        for i, row in enumerate(visited):
            if i % 2 != 1:
                row.reverse()
            output += row

        return output