# Longest Line of Consecutive One in Matrix
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal (go up) or anti-diagonal (do down).
# Example:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# => 3
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not any(M): return 0

        m, n = len(M), len(M[0])
        max_consec = 0
        col = [0] * n
        # j + i is fixed for one line
        # starting point goes from (0,0) to (m - 1, 0) then (m - 1, n - 1)
        diag = [0] * (m + n)
        # j - i is fixed for one line
        # starting point goes from (m - 1, 0) to (0, 0) then (0, n - 1)
        anti = [0] * (m + n)

        for i in range(m):
            row = 0
            for j in range(n):
                if M[i][j] == 1:
                    row += 1
                    col[j] += 1
                    diag[j + i] += 1
                    anti[j - i + m] += 1
                    max_consec = max(max_consec, row)
                    max_consec = max(max_consec, col[j])
                    max_consec = max(max_consec, diag[j + i])
                    max_consec = max(max_consec, anti[j - i + m])
                else:
                    row = 0
                    col[j] = 0
                    diag[j + i] = 0
                    anti[j - i + m] = 0

        return max_consec

