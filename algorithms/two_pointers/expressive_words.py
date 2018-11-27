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
        i = j = 0

        while i < len(S) and j < len(W):
            if S[i] != W[j]:
                return False

            char = S[i]

            cnt_S = 0
            while i < len(S) and S[i] == char:
                i += 1
                cnt_S += 1

            cnt_W = 0
            while j < len(W) and W[j] == char:
                j += 1
                cnt_W += 1
            # one char in W cannot be extended to 2 chars in S
            # but two same chars in W can be extended to 3+
            if cnt_S < cnt_W or (cnt_S == 2 and cnt_W == 1):
                return False

        return i == len(S) and j == len(W)
# test cases
# S = "heeellooo", words = ["hello", "hi", "helo"] => 1
# S = "zzzzzyyyyy", words = ["zzyy","zy","zyy"] => 3
