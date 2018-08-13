# Number Of Corner Rectangles
# Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
# Only the corners need to have the value 1, all four 1s used must be distinct.
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]
# => 9
# [[1, 1, 1, 1]]
# => 0
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not any(grid):
            return 0

        dp_set = []  # row idx => indices of ones
        ans = 0

        for y in range(len(grid)):
            ones = set(idx for idx, val in enumerate(grid[y]) if val)
            dp_set.append(ones)

            for prev in range(y):
                matches = len(dp_set[y] & dp_set[prev])
                if matches >= 2:
                    ans += matches * (matches-1) / 2  # pick 2 from n

        return ans
# O(m * n ^ 2) time, O(m * n) space
