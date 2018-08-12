# Minimum Window Subsequence
# Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
# A subsequence of a string has some of chars in that string in orginal order.
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there are multiple such minimum-length windows, return the one with the left-most starting index.
# S = "abcdebdde", T = "bde"
# => "bcde"

# NOT FIGURED OUT YET
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m, n = len(T), len(S)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(1, n + 1):
            dp[0][j] = j + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if T[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        start = 0
        min_len = n + 1
        for j in range(1, n + 1):
            if dp[m][j] != 0:
                if j - dp[m][j] + 1 < min_len:
                    start = dp[m][j] - 1
                    min_len = j - dp[m][j] + 1

        return '' if min_len == n + 1 else S[start:start + min_len]

# definition: dp[i][j] stores the starting index of the substring where T has length i and S has length j
# base case: dp[0][j]
# tansition: dp[i][j] = dp[i - 1][j - 1]  (T[i - 1] == S[j - 1])
#                     = dp[i][j - 1]      (else)
