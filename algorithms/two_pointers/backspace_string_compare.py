# Backspace String Compare
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, j = len(S) - 1, len(T) - 1
        back_s = back_t = 0
        # using or since there could be case when the extra chars
        # are cleared out in the end
        while i >= 0 or j >= 0:
            while i >= 0 and (back_s or S[i] == '#'):
                if S[i] == '#':
                    back_s += 1
                else:
                    back_s -= 1
                i -= 1

            while j >= 0 and (back_t or T[j] == '#'):
                if T[j] == '#':
                    back_t += 1
                else:
                    back_t -= 1
                j -= 1

            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False

            i -= 1
            j -= 1

        return i == j
# O(n) time, O(1) space
# test case:
# 1. "nzp#o#g", "b#nzp#o#g"  => true
# 2. "a##c", "#a#c" => true
# 3. "a#c", "b" => false
