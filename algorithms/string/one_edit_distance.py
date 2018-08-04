# One Edit Distance
# determine if two strings are one edit distance away
# one edit action can be insert / delete / replace a char
class Solution(object):
    def is_one_edit_distance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1: return False

        if len(s) == len(t):
            diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        if len(s) < len(t):
            return self.compare(s, t)
        else:
            return self.compare(t, s)

    def compare(self, shorter, longer):
        # len(longer) - len(shorter) == 1
        i = 0
        while i < len(shorter) and shorter[i] == longer[i]:
            i += 1
        # now shorter[i] is the first char that is different
        while i < len(shorter):
            if shorter[i] != longer[i + 1]:
                return False
            i += 1
        return True
