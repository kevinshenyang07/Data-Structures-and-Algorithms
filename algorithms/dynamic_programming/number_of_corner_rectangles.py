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
        if not any(grid): return 0

        ones_by_row = []  # row index => set of points on that row
        count = 0

        for i in range(len(grid)):
            ones_curr_row = set(j for j, val in enumerate(grid[i]) if val)
            ones_by_row.append(ones_curr_row)

            for prev in range(i):
                # worst case O(n), real world O(min(set1, set2))
                matches = len(ones_by_row[prev] & ones_by_row[i])
                if matches >= 2:
                    count += matches * (matches - 1) / 2  # pick 2 from n

        return count
# O(m ^ 2 * n) time, O(m * n) space
