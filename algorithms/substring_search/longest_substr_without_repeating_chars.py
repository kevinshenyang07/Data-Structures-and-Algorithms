class Solution(object):
    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        i = res = 0

        for j, char in enumerate(s):
            # if repeating char is in range of the pointers
            if char in char_index and i <= char_index[char]:
                i = char_index[char] + 1

            char_index[char] = j
            res = max(res, j - i + 1)

        return res
# O(n) time and space, one pass