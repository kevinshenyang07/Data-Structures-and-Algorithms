# Word Search
class Solution(object):
    def exist(self, board, word):
        if not any(board):
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        m, n = len(board), len(board[0])
        # end condition
        if word == '':
            return True
        # stop conditions
        if i < 0 or i >= m or j < 0 or j >= n or word[0] != board[i][j]:
            return False
        # mark visited, save as tmp
        tmp = board[i][j]
        board[i][j] = "#"
        # search each direction
        result = False
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if self.dfs(board, x, y, word[1:]):
                result = True
                break
        # restore the value of the current slot
        board[i][j] = tmp
        return result
