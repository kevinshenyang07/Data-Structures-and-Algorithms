# Ugly Number II
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5
class Solution(object):
    def nthUglyNumber(self, n):
        # ugly[i2] means the smallest ugly number (candidate) that when multiplied by 2,
        # will be greater than ugly[-1], and the same same applies for i3 and i5
        # first ugly number usually considered to be 1
        ugly = [1]
        i2 = i3 = i5 = 0

        while len(ugly) < n:

            next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            ugly.append(next_ugly)
            # the candidate must be in existing array
            if ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            if ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            if ugly[i5] * 5 <= ugly[-1]:
                i5 += 1

        return ugly[-1]
# O(n) time, O(n) space


if __name__ == '__main__':
    print Solution().nthUglyNumber(10)  # 12
