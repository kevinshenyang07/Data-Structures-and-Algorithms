# Unique Binary Search Trees
class Solution(object):
    def numTrees(self, n):
        """
        dp[i]: number of unique BST with width i

        dp[i] = 1                           i = 0 or 1
        dp[i] = sum(dp[j - i] * dp[i - j])  1 <= j <= i, j being the root
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]
