# Smallest Rectangle Enclosing Black Pixels
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
# The black pixels are connected, i.e., there is only one black region.
# Pixels are connected horizontally and vertically.
# Given the coordinate of one of the black pixels, return the area of the smallest rectangle that encloses all black pixels.
# [
#   ["0", "0", "1", "0"],
#   ["0", "1", "1", "0"],
#   ["0", "1", "0", "0"]
# ]
# x, y = 0, 2 ans = 6
class Solution(object):
    def minArea(self, image, x, y):
        if not any(image): return 0

        m, n   = len(image), len(image[0])
        row_has_one = lambda x: '1' in image[x]
        col_has_one = lambda y: any(row[y] == '1' for row in image)

        top    = self.bisect(0, x, row_has_one)
        bottom = self.bisect(x, m, lambda x: not row_has_one(x))
        left   = self.bisect(0, y, col_has_one)
        right  = self.bisect(y, n, lambda y: not col_has_one(y))

        return (bottom - top) * (right - left)

    # smallest index with check condition
    def bisect(self, lo, hi, check):
        while lo + 1 < hi:
            mid = lo + (hi - lo) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        if check(lo):
            return lo
        return hi
# O(logm + logn) time
# dfs would be O(mn) time
