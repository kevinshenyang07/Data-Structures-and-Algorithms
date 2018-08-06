# Palindromic Substrings
# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
# f("aaa") => 6 ("a", "a", "a", "aa", "aa", "aaa")

# DP solution
class SolutionV1(object):
    def countSubstrings(self, s):
        dp = [[0] * len(s) for _ in range(len(s))]  # if s[i:j+1] is palindromic

        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if i == j:  # base case 1
                    dp[i][j] = 1
                elif i + 1 == j:  # base case 2
                    dp[i][j] = int(s[i] == s[j])
                else:  # inductive function
                    dp[i][j] = int(dp[i+1][j-1] == 1 and s[i] == s[j])

        return sum([sum(row) for row in dp])  # can optimize with using a variable count
# O(n^2) time and space

# stop earlier
class SolutionV2(object):
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            count += self.extend_palindrome(s, i, i)  # substring length is odd
            count += self.extend_palindrome(s, i, i + 1)  # substring length is even
        return count

    def extend_palindrome(self, s, left, right):
        cnt = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            cnt += 1
            left -= 1
            right += 1
        return cnt
# O(n^2) time, O(1) space