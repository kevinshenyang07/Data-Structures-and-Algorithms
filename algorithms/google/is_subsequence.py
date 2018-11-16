# Is Subsequence
# Given a string s and a string t, check if s is subsequence of t.
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
# Followup:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
# and you want to check one by one to see if T has its subsequence.
# In this scenario, how would you change your code?
# What if there're lots of T instead?
class Solution(object):
    def isSubsequence(self, s, t):
        # this should be done before the call
        # can also cache completed query
        indices_map = collections.defaultdict(list)  # char => indices on t
        for i, char in enumerate(t):
            indices_map[char].append(i)

        j = -1  # smallest index found on T that makes s[i] == t[j]
        for char in s:
            if char not in indices_map:
                return False
            # j + 1 to be the smallest possible next index
            j = self.binary_search(indices_map[char], j + 1)
            if j == -1:
                return False

        return True

    # first index i on T that makes i >= target
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] >= target:
            return nums[left]  # different from template
        elif nums[right] >= target:
            return nums[right]
        else:
            return -1
# O(T) time for preprocessing, O(S * logT) time for query

