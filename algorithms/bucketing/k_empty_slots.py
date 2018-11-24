import math

# K Empty Slots
# There is a garden with N slots. In each slot, there is a flower.
# The N flowers will bloom one by one in N days.
# In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
# Given an array flowers consists of number from 1 to N.
# Each number in the array represents the place where the flower will open in that day.
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x,
# where i and x will be in the range from 1 to N.
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming,
# and also the number of flowers between them is k and these flowers are not blooming.
# If there isn't such day, output -1.

# brute force: on each day, when a flower blooms, look k distance back / forward
# which is O(nk) time, O(n) space
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers:
            return -1

        # partition slots into buckets with size to be k + 1
        # so that even the max - min element in one bucket would not qualify
        # range of bucket[0]: [1, k + 1], bucket[1]: [k + 2, 2k + 2] ...
        num_buckets = int(math.ceil(len(flowers) / (k + 1.0)))
        bucket_mins = [float('inf')] * num_buckets
        bucket_maxs = [float('-inf')] * num_buckets

        for i, pos in enumerate(flowers):
            # update the range of corresponding bucket on the go
            j = (pos - 1) / (k + 1)
            if pos <= bucket_mins[j]:
                bucket_mins[j] = pos
                # compare with left max
                if j > 0 and bucket_mins[j] - bucket_maxs[j - 1] == k + 1:
                    return i + 1
            if pos >= bucket_maxs[j]:
                bucket_maxs[j] = pos
                # compare with right min
                if j < num_buckets - 1 and bucket_mins[j + 1] - bucket_maxs[j] == k + 1:
                    return i + 1
            # if pos is between min and max, there won't be an answer for that flower

        return -1
# O(n) time, O(n/(k+1)) space
