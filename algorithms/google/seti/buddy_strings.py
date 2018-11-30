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
        if A == B and len(A) > len(set(A)):
            return True

        diff = []
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            diff.append((A[i], B[i]))
            if len(diff) > 2:
                return False
            if len(diff) == 2 and (B[i], A[i]) not in diff:
                return False

        return len(diff) == 2
# test cases:
# 1. 'ab', 'ba' => true
# 2. 'aa', 'aa' => true
# 3. '', 'aa' => false
# 4. 'abc', 'abd' => false
