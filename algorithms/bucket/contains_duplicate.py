# Contains Duplicate II
# find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i, num in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])
            if num in window:
                return True
            window.add(num)

        return False
# O(n) time, O(k) space


# Contains Duplicate III
# find out whether there are two distinct indices i and j in the array
# such taht the absolute difference between nums[i] and nums[j] is at most t
# and the absolute difference between i and j is at most k
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False

        # bucket index => last seen number in that bucket
        # each bucket being [i * t, (i + 1) * t), i = 0, 1, 2,...
        # each bucket only holds one number, otherwise there's duplicate
        buckets = {}

        for i, num in enumerate(nums):
            # maintain a window of size k
            if i > k:
                last_j = nums[i - k - 1] / (t + 1)
                buckets.pop(last_j)
            # duplicate can only appear in current or nearby buckets
            j = num / (t + 1)
            if j in buckets:
                return True
            if j - 1 in buckets and abs(num - buckets[j - 1]) <= t:
                return True
            if j + 1 in buckets and abs(num - buckets[j + 1]) <= t:
                return True
            buckets[j] = num

        return False
# O(n) time, O(n / (t + 1)) space
