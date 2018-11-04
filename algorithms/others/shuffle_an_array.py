#  Shuffle an Array
# Shuffle a set of numbers without duplicates.
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = len(self.nums)
        shuffled = [num for num in self.nums]
        # modern Knuth's algo
        for i in range(n):
            j = int(random.random() * n)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
# haven't found a good proof yet, but to generate a random permutation,
# each num has a probability of 1 / n to be at any index
