# Candy Crush
# description too long, search it online
class Solution(object):
    def candyCrush(self, board):
        while True:
            crushing = self.find_crushing(board)

            if not crushing:
                break

            for i, j in crushing:
                board[i][j] = 0

            self.drop(board)

        return board

    def find_crushing(self, board):
        m, n = len(board), len(board[0])
        crushing = []

        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    continue
                if self.should_crush(i, j, board):
                    crushing.append((i, j))
        return crushing

    def should_crush(self, i, j, board):
        m, n = len(board), len(board[0])
        # check lower two / upper two / left two / right two / in the middle vertically / in the middle horizontally
        return (i - 2 >= 0 and board[i][j] == board[i - 1][j] == board[i - 2][j]) or \
               (i + 2 < m and board[i][j] == board[i + 1][j] == board[i + 2][j]) or \
               (j - 2 >= 0 and board[i][j] == board[i][j - 1] == board[i][j - 2]) or \
               (j + 2 < n and board[i][j] == board[i][j + 1] == board[i][j + 2]) or \
               (i - 1 >= 0 and i + 1 < m and board[i - 1][j] == board[i][j] == board[i + 1][j]) or \
               (j - 1 >= 0 and j + 1 < n and board[i][j - 1] == board[i][j] == board[i][j + 1])

    def drop(self, board):
        m, n = len(board), len(board[0])
        # for each column
        for j in range(n):
            # board[k][j] being first candy that has not been processed
            k = m - 1
            # move remaining canides to bottom
            for i in range(m - 1, -1, -1):
                if board[i][j] > 0:
                    board[k][j] = board[i][j]
                    k -= 1
            # clean up
            for i in range(k, -1, -1):
                board[i][j] = 0
