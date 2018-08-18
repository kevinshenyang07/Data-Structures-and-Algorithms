# Game of Life
# assume board is valid
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                # 0: dead, 2: dead-to-live
                # 1: live, 3: live-to-dead
                cnt = self.count_live(i, j, board)
                if board[i][j] % 2 != 1:  # currently dead
                    if cnt == 3:
                        board[i][j] = 2
                elif cnt < 2 or cnt > 3:  # currently live but will be dead
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0

    def count_live(self, i, j, board):
        m, n = len(board), len(board[0])
        count = 0
        for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and board[x][y] % 2 == 1:
                count += 1
        return count
