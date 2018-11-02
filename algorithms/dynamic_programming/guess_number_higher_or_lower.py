# Guess Number Higher or Lower II
class Solution(object):
    def getMoneyAmount(self, n):
        """
        the strategy is to choose the option that if the worst consequence of that option occurs,
        it's the least worst case among all options

        specifically, if picking any number in a range, find the highest amount of money to pay,
        then choose the minimal highest amount (minmax)

        dp[i][j]: smallest amount of money to pay to win in guessing from i to j

        dp[i][i] = 0    no cost for one number
        dp[i][i+1] = i  pick the first in two numbers so that worst case is i

        dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]))  i < k < j
                      (if k is picked, check highest amount to pay if the answer is on the left or right)
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n):
            dp[i][i + 1] = i

        for width in range(3, n + 1):
            for i in range(1, n - width + 2):
                j = i + width - 1

                range_min = float('inf')
                for k in range(i + 1, j):
                    curr_max = k + max(dp[i][k - 1], dp[k + 1][j])
                    range_min = min(range_min, curr_max)

                dp[i][j] = range_min

        return dp[1][n]

