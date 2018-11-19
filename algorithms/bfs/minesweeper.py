# Minesweeper
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])
        delta = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        queue = collections.deque()
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            # count nearby mines
            mines = 0
            for dx, dy in delta:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'M':
                    mines += 1

            if mines > 0:
                board[x][y] = str(mines)
                # do not enqueue neighbor cells
            else:
                board[x][y] = 'B'
                for dx, dy in delta:
                    i, j = x + dx, y + dy
                    if 0 <= i <m and 0 <= j < n and board[i][j] == 'E':
                        board[i][j] = 'B'
                        queue.append((i, j))

        return board
