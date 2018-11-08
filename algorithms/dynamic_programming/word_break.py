# Word Break
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# The same word in the dictionary may be reused multiple times in the segmentation
class Solution(object):
    def wordBreak(self, s, words):
        """
        dp[i]: s[:i] have words matching in the dict
        dp[0] = True
        dp[i] = any(dp[i-len(w)] and s[i-len(w)] == w for w in words if len(w) <= i)
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in words:
                if len(word) <= i and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break

        return dp[n]
# test case 1:
# "applepenapple", ["apple", "pen"] => True
# test case 2:
# "catsandog", ["cats","dog","sand","and","cat"] => True


# Word Break II
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces
# in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
# The same word in the dictionary may be reused multiple times in the segmentation.
class Solution(object):
    def wordBreak(self, s, words):
        """
        memoized dfs much more intuitive
        """
        return self.dfs(s, words, {})

    def dfs(self, s, words, cache):
        if s in cache:
            return cache[s]

        result = []
        for word in words:
            if word == s:
                result.append(word)
            elif word == s[:len(word)]:
                sub_result = self.dfs(s[len(word):], words, cache)
                for r in sub_result:
                    result.append(word + ' ' + r)

        cache[s] = result
        return result
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# => [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
