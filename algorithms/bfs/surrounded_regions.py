# Surrounded Regions
# approach: introducing a new state 'T'
class Solution(object):
    def solve(self, board):
        if not any(board):
            return

        m, n = len(board), len(board[0])
        queue = collections.deque()

        # add coordinates on the edge
        for i in range(m):
            for j in [0, n - 1]:
                queue.append((i, j))
        for i in [0, m - 1]:
            for j in range(n):
                queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                # mark 'O's connected to the edge as 'T'
                board[i][j] = 'T'
                # add nearby slots
                for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                    queue.append((x, y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
