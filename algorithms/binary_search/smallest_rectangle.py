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
    def min_area(self, image, x, y):
        # smallest index with check condition
        def first(lo, hi, check):
            while lo < hi:
                mid = (lo + hi) / 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        if not any(image): return 0

        m, n   = len(image), len(image[0])
        top    = first(0, x, lambda x: '1' in image[x])
        bottom = first(x, m, lambda x: '1' not in image[x])
        left   = first(0, y, lambda y: any(row[y] == '1' for row in image))
        right  = first(y, n, lambda y: all(row[y] == '0' for row in image))

        return (bottom - top) * (right - left)
# dfs would be O(n) time
