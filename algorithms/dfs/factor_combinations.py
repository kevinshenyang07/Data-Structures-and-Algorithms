import math


# Factor Combinations
# return all possible combinations of its factors
# f(8) => [[2, 4], [2, 2, 2]]
# assume n to be positive
class Solution(object):
    def get_factors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(x, start, path):
            # end condition
            if len(path) > 0:
                result.append(path + [x])

            upper = int(math.sqrt(x))
            for i in range(start, upper + 1):
                if x % i == 0:
                    dfs(x / i, i, path + [i])

        result = []
        dfs(n, 2, [])
        return result
