# Candy
# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# 1. Each child must have at least one candy.
# 2. Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1] * len(ratings)
        # scan from left to right
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1
        # scan from right to left
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)

        return sum(candies)
# O(n) time and space
# illustration:
# [1, 3, 2, 2, 1]
# [1, 2, 1, 1, 1]  <= left to right
# [1, 2, 1, 2, 1]  <= right to left
