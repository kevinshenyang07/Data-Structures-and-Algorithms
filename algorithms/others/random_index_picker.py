# Random Pick Index
# Given an array of integers with possible duplicates, randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.
# The nums array can be very large, don't use O(n) memory.
# Each index should have equal probability of returning.
# Approach: reservoir sampling
class RandomIndexPicker(object):

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        picked = -1
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if 1.0 / count > random.random():
                    picked = i
        return picked
# O(n) time, O(1) space
# proof:
# say there're k numbers equal to target, 1 <= i <= k
# p(picked == i) = (1 / i)            p(initially picked i)
#                * (i / i + 1)        p(then i + 1 not picked)
#                * (i + 1 / i + 2)    p(then i + 2 not picked)
#                * ...
#                * (k - 2 / k - 1)    p(then k - 1 not picked)
#                * (k - 1 / k)        p(then k not picked)
#                = 1 / k
# example:
# say we have 4 '1's  in the array, the first index with value '1' has p == 1 to be picked,
# the second has p == 1 / 2, the third has p == 1 / 3, the last has p == 1 / 4
# p(picked == 2) = (1 / 2) * (2 / 3) * (3 / 4)


# randomly smaple k elements
class RandomSampler(object):

    def __init__(self, nums):
        self.nums = nums

    def sample(self, k):
        reservoir = nums[:k]
        for i, num in enumerate(nums):
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = i
        return reservoir
# O(n) time, O(1) extra space
# p(nums[0] in reservoir) = (1 / 1)
#                         * (1 / 2)
#                         * (2 / 3)
#                         * ...
#                         = (k - 2 / k -1)
#                         = (k - 1 / k)
#                         = 1 / k
