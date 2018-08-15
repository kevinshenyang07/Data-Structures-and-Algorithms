# Rectangle Overlap
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates
# of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.
# Two rectangles overlap if the area of their intersection is positive.
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1 = rec1[0], rec1[1]
        x2, y2 = rec1[2], rec1[3]
        i1, j1 = rec2[0], rec2[1]
        i2, j2 = rec2[2], rec2[3]

        return not (x1 >= i2 or x2 <= i1 or y1 >= j2 or y2 <= j1)


# Rectangle Area
# Find the TOTAL area covered by two rectilinear rectangles in a 2D plane.
# note that in this x-y plane, x is smaller going down
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :rtype: int
        """
        xs = sorted([A, C, E, G])
        ys = sorted([B, D, F, H])

        overlapped = 0
        if not (A >= G or B >= H or C <= E or D <= F):
            overlapped = abs(xs[1] - xs[2]) * abs(ys[1] - ys[2])

        return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H) - overlapped
