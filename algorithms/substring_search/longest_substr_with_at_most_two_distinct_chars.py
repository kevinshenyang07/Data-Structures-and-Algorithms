class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 2:
            return len(s)

        chars = set([])
        i = I = J = 0

        for j, char in enumerate(s):
            if char not in chars:
                if len(chars) < 2:
                    chars.add(char)
                else:
                    # use s[j-1] and s[j] as the base new possible ans
                    chars = set([s[j-1], char])
                    # and expand left as far as possible
                    i = j - 1
                    while i >= 0 and s[i-1] == s[j-1]:
                        i -= 1

            if j - i > J - I:
                I, J = i, j

        return J - I + 1