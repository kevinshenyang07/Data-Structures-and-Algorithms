# Isomorphic Strings
# Two strings are isomorphic if the characters in s can be replaced to get t.
# assume s and t have the same length, note that multiple chars cannot map to one char
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

# followup: given a 'words' list, and a target string, find out the isomorphic strings in the list
# approach: if a word A is isomorphic to another word B in words, and B is isomorphic to
#           the target string, then A is isomorphic to the target string two
#           => uf.union(A, B) if isIsomorpthic(A, B)
