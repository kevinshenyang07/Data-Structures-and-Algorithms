from union_find import UnionFind

# Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        n = len(nums)
        uf = UnionFind(n)
        pos = {}  # num => index

        for i, num in enumerate(nums):
            # skip duplicate numbers
            if num in pos:
                continue

            pos[num] = i
            # always union into larget group
            if num - 1 in pos:
                uf.union(pos[num - 1], i)
            if num + 1 in pos:
                uf.union(pos[num + 1], i)

        return max(uf.sizes)
# O(n) time and space
# [] => 0
# [100,4,200,1,3,2,5] => 5
