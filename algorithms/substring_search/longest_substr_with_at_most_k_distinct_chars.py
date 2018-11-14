# Longest Substring with At Most K Distinct Characters
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        i = 0
        mapping = {}  # char => largest index of this char appears so far

        for j, char in enumerate(s):
            # include current char first then eject if needed
            mapping[char] = j

            if len(mapping) > k:
                k = min(mapping.values())
                mapping.pop(s[k])
                i = k + 1

            max_length = max(max_length, j - i + 1)

        return max_length
