# Valid Tic-Tac-Toe State
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        # balance of turns, number of pieces on each row / col / diag
        # +1 indicates a turn / a piece of X, -1 => O
        turns = 0
        rows, cols = [0] * 3, [0] * 3
        diag = antidiag = 0

        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    turns += 1
                    rows[i] += 1
                    cols[j] +=1
                    if i == j:
                        diag += 1
                    if i + j == 2:
                        antidiag += 1
                elif board[i][j] == 'O':
                    turns -= 1
                    rows[i] -= 1
                    cols[j] -= 1
                    if i == j:
                        diag -= 1
                    if i + j == 2:
                        antidiag -= 1

        xwin = 3 in rows or 3 in cols or diag == 3 or antidiag == 3
        owin = -3 in rows or -3 in cols or diag == -3 or antidiag == -3

        # difference of X and O moves must be in range of [0, 1]
        if turns not in (0, 1):
            return False
        # first player has already won
        if turns == 0 and xwin:
            return False
        # second player has already won
        if turns == 1 and owin:
            return False
        return True
