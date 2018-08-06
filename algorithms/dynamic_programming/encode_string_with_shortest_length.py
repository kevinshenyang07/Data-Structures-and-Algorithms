# Encode String with Shortest Length
# Given a non-empty string, encode the string such that its encoded length is the shortest.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
# Note:
# 1. k will be a positive integer and encoded string will not be empty or have extra space.
# 2. The input string contains only lowercase English letters.
# 3. If an encoding process does not make the string shorter, then do not encode it.
# 4. If there are several solutions, return any of them is fine.
# Example:
# f('aaa') => 'aaa'
# f('aaaaa') => '5[a]'
# f('aabcaabcd') => '2[aabc]d'
class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[''] * n for _ in range(n)]

        # starting from substr with length == 1, 2, 3...
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                substr = s[i:j+1]  # inclusive range
                dp[i][j] = substr  # initialize with original substring

                if j - i >= 4:

                    # break it down further with solved sub-problems
                    for k in range(i, j):
                        left = dp[i][k]
                        right = dp[k+1][j]
                        if len(left) + len(right) < len(dp[i][j]):
                            dp[i][j] = left + right

                    # find if the whole substr can be constructed by a repeat_str
                    for k in range(len(substr)):
                        repeat_str = substr[:k+1]
                        if len(substr) % (k + 1) == 0 and not substr.replace(repeat_str, ''):
                            repeat_times = len(substr) / (k + 1)
                            encoded = "{}[{}]".format(repeat_times, dp[i][i+k])  # use encoded repeat_str
                            if len(encoded) < len(dp[i][j]):
                                dp[i][j] = encoded

        return dp[0][n-1]
# O(n^3) time and space
