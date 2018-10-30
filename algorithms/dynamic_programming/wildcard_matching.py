# Wildcard Matching
class Solution(object):
    def isMatch(self, s, p):
        """
        dp[i][j]: if s[:i+1] is matched by p[:j+1]

        dp[0][0] = true
        dp[0][j] = p[j - 1] == '*'
        dp[i][0] = s == ''

        dp[i][j] = dp[i - 1][j - 1]                each last char of s and p matches
                 = dp[i - 1][j] or dp[i][j - 1]    '*' is considered as empty or matches one or more chars in s[:i+1]
        """
        if not s or not p:
            return s == p or p == '*'

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[-1][-1]
