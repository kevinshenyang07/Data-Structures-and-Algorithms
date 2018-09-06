import random

# Random Pick with Weight
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.acc_w = [w[0]]  # prefix sum of weights
        for i in range(1, len(w)):
            weight = self.acc_w[-1] + w[i]
            self.acc_w.append(weight)

    def pickIndex(self):
        """
        :rtype: int
        """
        num = random.randint(1, self.acc_w[-1])

        left, right = 0, len(self.acc_w) - 1
        while left < right:
            mid = left + (right - left) / 2
            if self.acc_w[mid] < num:
                left = mid + 1
            elif self.acc_w[mid] > num:
                right = mid
            else:
                return mid
        # self.acc_w[left] < num < self.acc_w[right]
        return left

