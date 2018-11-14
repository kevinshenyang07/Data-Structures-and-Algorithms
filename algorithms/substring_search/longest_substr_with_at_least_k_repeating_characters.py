# Longest Substring with At Least K Repeating Characters
# Find the length of the longest substring T of a given string (consists of lowercase letters only)
# such that every character in T appears no less than k times.
# s = "ababbc", k = 2 => 5 ("ababb")
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or len(s) < k:
            return 0
        if k == 0:
            return len(s)

        counter = collections.Counter(s)
        # another base case: no infrequent substrings
        if all(counter[char] >= k for char in s):
            return len(s)
        # 'split' s with those infrequent substrings
        # the answer must be among the 'splitted' substrings
        max_len = 0
        i = 0
        for j, char in enumerate(s):
            if counter[char] < k:
                max_len = max(max_len, self.longestSubstring(s[i:j], k))
                i = j + 1
        # check last element of 'splitted' substrings
        max_len = max(max_len, self.longestSubstring(s[i:], k))

        return max_len
# O(n) time and space
