# Add Bold Tag in String
# Given a string s and a list of strings words, you need to add a closed pair of bold tag
# <b> and </b> to wrap the substrings in s that exist in dict.
# If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag.
# Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
# Example:
# s = "aaabbcc"
# words = ["aaa","aab","bc"]
# => "<b>aaabbc</b>c"

# assume words won't contain duplicates
class Solution(object):
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        bold = [False] * len(s)

        # index can't jump or skip since there is overlappign words
        right = -1  # last index so far of the char that should be bold
        for i in range(len(s)):
            for word in words:
                if s.startswith(word, i):
                    right = max(right, i + len(word) - 1)
            bold[i] = i <= right

        res = []
        for i in range(len(s)):
            if bold[i]:
                if i == 0 or not bold[i-1]:
                    res.append('<b>')
                res.append(s[i])
                if i == len(s) - 1 or not bold[i+1]:
                    res.append('</b>')
            else:
                res.append(s[i])

        return ''.join(res)
# note: words can be matched for multiple times
# O(n * c) time, O(n) space, with n being length of s, c being total chars in words
