import math

# Factor Combinations
# return all possible combinations of its factors
# f(8) => [[2, 4], [2, 2, 2]]
# assume n to be positive
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(n, 2, [])
        return self.result

    def dfs(self, x, start, path):
        # end condition
        if len(path) > 0:
            self.result.append(path + [x])

        upper = int(math.sqrt(x))
        for i in range(start, upper + 1):
            if x % i == 0:
                self.dfs(x / i, i, path + [i])
