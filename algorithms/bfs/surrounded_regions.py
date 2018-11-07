# Surrounded Regions
# approach: introducing a new state 'T' that indicates
# the 'O' cell is connected an 'O' cell on the border
class Solution(object):
    def solve(self, board):
        if not any(board):
            return

        m, n = len(board), len(board[0])
        queue = collections.deque()

        # add coordinates on the border
        # avoid doing BFS on every cell, use only one queue
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))

        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            board[i][j] = 'T'

            for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    queue.append((x, y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
