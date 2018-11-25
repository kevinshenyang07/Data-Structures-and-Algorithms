# Buddy Strings
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        diff_chars = []
        for i in range(len(A)):
            if A[i] != B[i]:
                if not diff_chars:
                    diff_chars.append((A[i], B[i]))
                elif len(diff_chars) == 2:
                    return False
                elif diff_chars[0] != (B[i], A[i]):
                    return False
                else:
                    diff_chars.append((A[i], B[i]))

        return len(diff) == 2 or len(A) > len(set(A))
# test cases:
# 1. 'ab', 'ba' => true
# 2. 'aa', 'aa' => true
# 3. '', 'aa' => false
# 4. 'abc', 'abd' => false
