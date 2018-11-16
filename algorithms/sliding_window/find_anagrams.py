# Find Anagrams
# Given a string s and a non-empty string t, find all the start indices of t's anagrams in s.
class Solution(object):
    def findAnagrams(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: List[int]
        """
        if len(s) < len(t):
            return []

        result = []
        # if the balance of char counts are all 0 then a substring is anagram to t
        balance = collections.Counter(t)

        for i, char in enumerate(s):
            # when a char moves in, update the count
            balance[char] = balance.get(char, 0) - 1
            # when a char moves out of the window, add the count back
            if i >= len(t):
                char_out = s[i - len(t)]
                balance[char_out] += 1
            # check the requirement of the problem
            if all(v == 0 for v in balance.values()):
                result.append(i - len(t) + 1)
        return result
# since the balance dict contains only a limited set of keys
# the call of all() can be treated as O(1) operation
# thus making it O(n) time and O(1) space
