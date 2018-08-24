import math

# Permutation Sequence
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# Given n and k, return the kth permutation sequence.
# f(4, 9) => "2314"
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(1, n + 1)
        digits = []
        k -= 1  # change to zero-indexing

        for i in range(n - 1, -1, -1):
            fact = math.factorial(i)
            pos = k / fact
            k = k % fact

            digit = nums[pos]
            digits.append(digit)
            nums.remove(digit)

        return ''.join(str(digit) for digit in digits)
