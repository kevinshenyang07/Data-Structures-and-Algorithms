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
        char_index = {}  # char => largest index of this char appears so far

        for j, char in enumerate(s):
            char_index[char] = j

            if len(char_index) > k:
                i = min(char_index.values())  # earliset removable char
                del char_index[s[i]]
                i += 1

            max_length = max(max_length, j - i + 1)

        return max_length
