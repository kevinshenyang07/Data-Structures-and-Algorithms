# Paint House II
# There are a row of n houses, each house can be painted with one of the k colors.
# The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by a n x k cost matrix.
# Find the minimum cost to paint all houses.
# f([[1,5,3],[2,9,4]]) => 5

# assume costs are positive and length of elements in costs are all 3
class Solution(object):
    def min_cost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not any(costs):
            return 0

        n, k = len(costs), len(costs[0])
        dp = costs[0]  # only for getting smallest two
        m1, m2 = self.smallest_two(dp)

        for i in range(1, n):
            for j in range(k):
                # lowest accumulative cost previously
                min_prev = m2 if dp[j] == m1 else m1
                dp[j] = min_prev + costs[i][j]
            m1, m2 = self.smallest_two(dp)

        return m1

    def smallest_two(self, arr):
        m1 = m2 = float('inf')
        for val in arr:
            if val < m1:
                m1, m2 = val, m1
            else:
                m2 = min(m2, val)
        return m1, m2
# O(nk) time, O(k) space
# to optimize space, use previous row in costs to store dp

# thought process
# since current state only depends on previous state
# => dp: lowest acc cost until house i with color j
#      = minimum of acc costs until house i-1 with last house not using color j
#      + cost of using color j on house i
# => smallest two acc costs are needed to get next lowest costs
