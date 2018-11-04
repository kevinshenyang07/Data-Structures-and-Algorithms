# Distinct Subsequences
class Solution(object):
    def numDistinct(self, s, t):
        """
        dp[i][j]: how many distinct subseqs of s[:i] matches t[:j]

        dp[i][0] = 1            only one subseq of s matches an empty strign
        dp[0][j] = 0  j >= 1    no subseqs of an empty string matches t

        dp[i][j] = dp[i - 1][j] + dp[i- 1][j - 1]    s[i] == t[j]
                 = dp[i - 1][j]                      s[i] != t[j]
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    #            using t[j - 1] + not using t[j - 1] but s[:i-1] still matches t[j]
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # distinct subseqs comes from s[:i-1]
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]
# find out the state transition function by hand:
#     r b i t
#   1 0 0 0 0
# r 1 1 0 0 0
# b 1 1 1 0 0
# b 1 1 2 0 0
# i 1 1 2 2 0
# t 1 1 2 2 2
