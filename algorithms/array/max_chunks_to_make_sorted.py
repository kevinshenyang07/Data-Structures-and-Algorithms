# Max Chunks To Make Sorted
# Given an array nums that is a permutation of [0, 1, ..., nums.length - 1], we split the array
# into some number of "chunks" (partitions), and individually sort each chunk.
# After concatenating them, the result equals the sorted array.
# What is the most number of chunks we could have made?
# Example:
# f([4,3,2,1,0]) => 1
# f([1,0,2,3,4]) => 4
# Approach:
# naturally range(n) is the sorted array, to make a chunk it has to satisfy below condition:
# sorted(nums[l:r+1]) == range(l, r+1), and since the previous chunk must satisfy the same condition,
# it can extended to sorted(nums[:r+1]) == range(r+1)
# then extended to nums[r] == r
class Solution(object):
    def maxChunksToSorted(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not any(nums): return 0

        max_chunks = 0
        curr_right = 0  # right bound of current window

        for i, num in enumerate(nums):
            curr_right = max(curr_right, num)
            # sorted(nums[:i+1]) == range(i+1)
            if curr_right == i:
                max_chunks += 1

        return max_chunks


# Max Chunks To Make Sorted II
# this time nums is no longer a permutation of range(n)
# the element can be in range(10**8) and can have duplicates
class Solution(object):
    def maxChunksToSorted(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not any(nums): return 0

        copied = sorted(nums)
        bal = {}  # balance of appeared numbers
        max_chunks = 0

        for i, num in enumerate(nums):
            bal[num] = bal.get(num, 0) + 1
            if bal[num] == 0:
                bal.pop(num)

            bal[copied[i]] = bal.get(copied[i], 0) - 1
            if bal[copied[i]] == 0:
                bal.pop(copied[i])

            if not bal:
                max_chunks += 1

        return max_chunks
