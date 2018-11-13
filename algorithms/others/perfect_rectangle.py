# Perfect Rectangle
# Steps:
# 1. check if the total area of the small rectangles == area of the larger rectangle
#    => overlaps, missing area
# 2. check if there're are 4 corners and they're the corners of the larger rectangle
#    => passed first check but is actually because of overlaps
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if not any(rectangles):
            return False

        x1 = y1 = float('inf')
        x2 = y2 = float('-inf')
        counter = collections.defaultdict(int)  # coor => occurrences
        total_area = 0

        for i, j, r, c in rectangles:
            x1 = min(x1, i)
            y1 = min(y1, j)
            x2 = max(x2, r)
            y2 = max(y2, c)

            total_area += (r - i) * (c - j)

            counter[(i, j)] += 1
            counter[(i, c)] += 1
            counter[(r, j)] += 1
            counter[(r, c)] += 1

        # if a coor is in the larger rectangle, it should appear 2 or 4 times
        corners = set(coor for coor in counter if counter[coor] % 2 == 1)
        expected_corners = set([(x1, y1), (x1, y2), (x2, y1), (x2, y2)])

        if total_area != (x2 - x1) * (y2 - y1):
            return False
        return corners == expected_corners
