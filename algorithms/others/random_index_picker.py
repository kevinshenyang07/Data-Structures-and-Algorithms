import random

# Random Pick Index
# the nums array can be very large, don't use O(n) memory
# each index should have equal probability of returning
# approach: reservoir sampling
class RandomIndexPicker(object):

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        picked = None
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # randint() inclusive on both sides
                if count == random.randint(1, count):
                    picked = i
        return picked
# assume there're k numbers equal to target, 1 <= i <= k
# p(picked == i) = (1 / i)
#                * (i / i + 1 )
#                * (i + 1 / i + 2)
#                * ...
#                * (k - 2 / k - 1)
#                * (k - 1 / k)
#                = 1 / k
