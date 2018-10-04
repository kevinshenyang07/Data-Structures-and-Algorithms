# Cracking the Safe
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = '0' * n
        visited = set([res])

        for _ in range(pow(k, n) - 1):
            # use len(res) - n + 1 to handle when n == 1
            prefix = res[len(res) - n + 1:]

            for i in range(k - 1, -1, -1):
                candidate = prefix + str(i)

                if candidate not in visited:
                    visited.add(candidate)
                    res += str(i)
                    break

        return res
# approach:
# 1. start from all zeros
# 2. to make a shortest string, reuse last n - 1 digits each time for new combination
# 3. start from largest digit so that candidates with larger distance from zeros
#    are visited first, then the ones in the middle

# example:
# n = 2, k = 3
# 0022120110
# 00
#  02
#   22
#    21
#     12
#      20
#       01
#        11
#         10
# can be also considered as path from column to column:
# 0 - 0
# 1 - 1
# 2 - 2
