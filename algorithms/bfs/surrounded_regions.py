# Surrounded Regions
# approach: introducing a new state 'T' that indicates
# the 'O' cell is connected an 'O' cell on the border
class Solution(object):
    def solve(self, board):
        if not any(board):
            return

        m, n = len(board), len(board[0])
        queue = collections.deque()

        # add coordinates on the boarder
        for i in range(m):
            for j in [0, n - 1]:
                queue.append((i, j))
        for i in [0, m - 1]:
            for j in range(n):
                queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                    queue.append((x, y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
