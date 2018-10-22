# Longest Substring with At Most K Distinct Characters
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        left = 0  # [left, i] is the current valid window
        mapping = {}  # char => largest index of this char appears so far

        for i, char in enumerate(s):
            mapping[char] = i

            if len(mapping) > k:
                j = min(mapping.values())
                mapping.pop(s[j])
                left = j + 1

            max_length = max(max_length, i - left + 1)

        return max_length
