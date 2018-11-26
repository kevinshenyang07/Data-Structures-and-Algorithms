class Go(object):
    def __init__(self, board):
        self.board = board

    # Q1
    # a white piece is dead only if it's surrounded by black pieces on four directions
    # or all nearby white pieces are surrounded by black pieces (no empty spot)
    def is_alive(self, i, j):
        self.visited = set()
        return self.dfs(i, j)

    def dfs(self, i, j):
        m, n = len(board), len(board[0])
        self.visited.add((i, j))

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in self.visited:
                if self.board[x][y] == '_':
                    return True
                if self.board[x][y] == self.board[i][j] and self.dfs(x, y):
                    return True

        return False

    # Q2
    # a white piece is surrounded if
    # 1. the white piece is at corner and two black pieces are surrounded
    # 2. otherwise, the surrounding black pieces (possibly plus border) form a circle
    def is_surrounded(self, i, j):
        pass
