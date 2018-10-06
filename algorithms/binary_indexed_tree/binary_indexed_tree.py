# divide and calculate range in bit
# 0 to n - 1 are mapped to 1 to n in self.sums
# i passed to both #update and #query is the original index
# since other class should not know about this mapping
class BIT(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)

    def accumulate(self, i, diff):
        i += 1
        while i <= self.n:
            self.sums[i] += diff  # new_val - curr_val
            i += (i & -i)

    def query(self, i):
        i += 1
        prefix_sum = 0  # sum from range [0, i] per se
        while i > 0:
            prefix_sum += self.sums[i]
            i -= (i & -i)
        return prefix_sum
# O(logn) for #accumulate and #query
#
# sums[i] = sum of the original values of the whole subtree on i
# sums[4] = nums[1-1] + nums[2-1] + nums[3-1] + nums[4-1]
# sums[6] = nums[6-1] + nums[5-1]
#
# lowbit (x & -x):
# f(5) = 1,       f(6) = 2
# f('101') = '1', f('110') = '10'
# => the least significant ‘1’ bit in a binary number
# => the largest power of 2 that divides into x
#
# https://www.youtube.com/watch?v=WbafSgetDDk draw this visualization in interview
#

class BIT2D(object):
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]

    def accumulate(self, i, j, diff):
        r, c = i + 1, j + 1
        while r <= self.m:
            while c <= self.n:
                self.sums[r][c] += diff
                c += (c & -c)
            r += (r & -r)
            c = j + 1

    def query(self, i, j):
        r, c = i + 1, j + 1
        area_sum = 0
        while r > 0:
            while c > 0:
                area_sum += self.sums[r][c]
                c -= (c & -c)
            r -= (r & -r)
            c = j + 1
        return area_sum
# O(logm * logn) for #accumulate and #query
