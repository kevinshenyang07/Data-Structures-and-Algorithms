# Image Overlap
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        translations = {}
        ones_a = []
        ones_b = []

        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    ones_a.append((i, j))
                if B[i][j] == 1:
                    ones_b.append((i, j))

        for i1, j1 in ones_a:
            for i2, j2 in ones_b:
                # group matching ones by shift
                shift = (i1 - i2, j1 - j2)
                translations[shift] = translations.get(shift, 0) + 1

        return max(translations.values() or [0])
