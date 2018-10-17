# Expressive Words
# For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.
# Note that we cannot extend a group of size one like "h" to a group of size two like "hh",
# all extensions must leave the group extended - ie., at least 3 characters long.
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        return sum(self.is_expressive(S, W) for W in words)

    def is_expressive(self, S, W):
        j, n = 0, len(W)  #

        for i in range(len(S)):
            if j < n and S[i] == W[j]:
                j += 1
            # if S[i] is not a stretched word, it cannot be compressed to W[j - 1]
            # S[-2:2] == ''
            elif S[i - 2:i + 1] != S[i] * 3 and S[i - 1:i + 2] != S[i] * 3:
                return False
        return j == n
# test cases
# S = "heeellooo", words = ["hello", "hi", "helo"] => 1
# S = "zzzzzyyyyy", words = ["zzyy","zy","zyy"] => 3
