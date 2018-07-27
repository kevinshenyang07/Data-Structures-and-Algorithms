# Sort Transformed Array
# Given a sorted array of integers nums and integer values a, b and c,
# apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array,
# return the result in sorted order.
# f([-4, -2, 2, 4], -1, 3, 5) => [-23, -5, 1, 7]
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        n = len(nums)
        i, j = 0, n - 1
        res = [0] * n
        k = n - 1 if a >= 0 else 0  # index on the res array

        # if a >= 0, one of values on both ends must be biggest
        # if a < 0, one of values on both ends must be smallest
        while i <= j:
            val_i = self.quad(nums[i], a, b, c)
            val_j = self.quad(nums[j], a, b, c)
            if a >= 0:
                if val_i >= val_j:
                    res[k] = val_i
                    i += 1
                else:
                    res[k] = val_j
                    j -= 1
                k -= 1
            else:
                if val_i >= val_j:
                    res[k] = val_j
                    j -= 1
                else:
                    res[k] = val_i
                    i += 1
                k += 1
        return res

    def quad(self, x, a, b, c):
        return a * x * x + b * x + c
# O(n) time, O(1) extra space
