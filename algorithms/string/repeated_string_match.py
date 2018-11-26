import math

# Repeated String Match
# Given two strings A and B, find the minimum number of times A has to be repeated
# such that B is a substring of it. If no such solution, return -1.

class Solution(object):
    def repeatedStringMatch(self, A, B):
        if not A or not B:
            return -1
        # lowest times A needs to be repeated
        repeating_times = int(math.ceil(float(len(B)) / len(A)))

        for i in range(2):
            # optimized python substring search
            if B in A * (repeating_times + i):
              return repeating_times + i
        return -1
# O(m * n) time, O(n) space


class SolutionV2(object):
    def repeatedStringMatch(self, A, B):
        m, n = len(A), len(B)
        # basically a modified version of string find
        # which does not stop at the end of A
        # but continue matching by looping through A
        for i in range(len(A)):
            j = 0
            while j < n and A[(i + j) % m] == B[j]:
                j += 1
            if j == n:
                return int(math.ceil((i + j) / float(m)))

        return -1
# O(m * n) time, O(1) space


if __name__ == '__main__':
    solution = Solution()
    f = solution.repeatedStringMatch
    print f('', 'abc')  # -1
    print f('abc', '')  # -1
    print f('abc', 'bcabcad')  # -1
    print f('adc', 'bcabcad')  # -1
    print f('abc', 'ab')  # 1
    print f('a', 'aa')  # 2
    print f('aaac', 'aac')  # 1
    print f('abc', 'bcabcab')  # 3
    print f('abc', 'abcabcab')  # 3
