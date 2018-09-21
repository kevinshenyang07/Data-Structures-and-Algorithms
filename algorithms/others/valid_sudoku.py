# Valid Sudoku
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        # index blocks by its upper left number
        blocks = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue

                num = board[i][j]
                # validate row
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)
                # validate col
                if num in cols[j]:
                    return False
                else:
                    cols[j].add(num)
                # validate block
                x, y = i // 3, j // 3
                if num in blocks[x][y]:
                    return False
                else:
                    blocks[x][y].add(num)

        return True
