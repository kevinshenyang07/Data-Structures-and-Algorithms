# Isomorphic Strings
# Two strings are isomorphic if the characters in s can be replaced to get t.
# assume s and t have the same length
# f('paper', 'title') => true
# f('foo', 'bar') => false
# f('aa', 'ba') => false
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}  # char from s to t
        d2 = {}  # char from t to s

        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = t[i]
            if t[i] not in d2:
                d2[t[i]] = s[i]
            if s[i] != d2[t[i]] or t[i] != d1[s[i]]:
                return False

        return True
