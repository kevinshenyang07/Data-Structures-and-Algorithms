# Student Attendance Record II
class Solution(object):
    def checkRecord(self, n):
        """
        dp[i]: the number of all possible attendance (without 'A') records with length i
               end with "P": dp[i-1]
               end with "PL": dp[i-2]
               end with "PLL": dp[i-3]
               end with "LLL": is not allowed

        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        the number of all possible attendance (with 'A') records with length n:
        ∑dp[i] *dp[n-1-i] i = 0,1,...,n-1
        """
        if n == 1:
            return 3
        if n == 0:
            return 0

        nums = [1, 1, 2]
        i = 2
        mod = 10 ** 9 + 7

        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2]) % mod)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % mod
        for i in range(n):
            result += nums[i+1] * nums[n-i] % mod
        return result % mod
# O(n) time and space
