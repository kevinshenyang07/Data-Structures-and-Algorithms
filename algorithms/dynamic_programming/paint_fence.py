# Paint Fence
# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# f(3, 2) => 6
class Solution(object):
    def num_ways(self, n, k):
        if n == 0: return 0
        if n == 1: return k

        # number of combinations when last two posts use the same / different colors
        same = k
        diff = k * (k - 1)

        for i in range(2, n):
            # same + diff = f(n-1), k - 1 since painting diff
            same, diff = diff, (same + diff) * (k - 1)

        return same + diff
