# Longest Repeating Character Replacement
# Given a string that consists of only uppercase English letters,
# you can replace any letter in the string with another letter at most k times.
# Find the length of a longest substring containing all repeating letters
# you can get after performing the above operations.
# s = "AABABBA", k = 1 => 4
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window = {}
        max_len = 0
        max_cnt = 0  # maximum number of chars in the window
        left = 0  # start of the window

        for i, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            max_cnt = max(max_cnt, window[char])

            while i - left + 1 > max_cnt + k:
                window[s[left]] -= 1
                left += 1
            max_len = max(max_len, i - left + 1)

        return max_len
