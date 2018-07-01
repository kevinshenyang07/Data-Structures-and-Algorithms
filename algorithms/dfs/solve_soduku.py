class Solution(object):
    def solve_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        self.solve(board)

    def solve(self, board):
        i, j = self.nextLoc(board)
        if i == -1 and j == -1:
            return True
        for num in '123456789':
            if self.isValid(i, j, num):
                board[i][j] = num
                if self.solve():
                    return True
                board[i][j] = '.'  # initialize value if solution not valid
        return False

    # can be optimized to find location with least possible candidates
    def nextLoc(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    return i, j
        return -1, -1

    def isValid(self, board, i, j, num):
        return self.validRow(board, i, num) and self.validCol(board, j, num) and self.validBox(board, i, j, num)

    def validRow(self, board, i, num):
        return num not in board[i]

    def validCol(self, board, j, num):
        for x in range(len(board)):
            if board[x][j] == num:
                return False
        return True

    def validBox(self, board, i, j, num):
        box_i, box_j = i / 3 * 3, j / 3 * 3  # upper left
        for x in range(box_i, box_i + 3):
            for y in range(box_j, box_j + 3):
                if board[x][y] == num:
                    return False
        return True