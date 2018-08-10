# On an NxN chessboard, a knight starts at the r-th row and c-th column
# and attempts to make exactly K moves. The rows and columns are 0 indexed,
# so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
# A chess knight has 8 possible moves it can make, each time the knight is to move,
# it chooses one of eight possible moves uniformly at random (even if it's off board) and moves there.
# The knight continues moving until it has made exactly K moves or has moved off the chessboard.
# Return the probability that the knight remains on the board after it has stopped moving.
# f(3, 2, 0, 0) => 0.0625
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[[0] * N for _ in range(N)] for _ in range(K + 1)]
        dp[0][r][c] = 1
        moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

        # bottom-up
        for k in range(K):
            for x in range(N):
                for y in range(N):
                    for dx, dy in moves:
                        i, j = x + dx, y + dy
                        if 0 <= i < N and 0 <= j < N:
                            # there's dp[k][x][y] ways from (x, y) to (i, j) at step k
                            dp[k+1][i][j] += dp[k][x][y]

        valid_moves = 0
        for row in dp[K]:
            valid_moves += sum(row)

        # the question implies the base is 8 ^ K even the knight could stop early
        return valid_moves / (8.0 ** K)

# dp[k][i][j]: how many ways to move to position (i, j) after k moves
# dp[k][i][j] = sum(dp[k-1][x][y]), for all (x, y) that can move to (i, j)
# O(K * N ^ 2) time and space
