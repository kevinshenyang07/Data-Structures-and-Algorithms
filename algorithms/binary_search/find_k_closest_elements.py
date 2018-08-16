# Find K Closest Elements
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        idx = self.binary_search(arr, x)

        left = right = idx
        while right - left + 1 < k:
            # pick left - 1 or right + 1
            if left == 0:
                right += 1
            elif right >= len(arr) - 1:
                left -= 1
            elif abs(arr[left-1] - x) <= abs(arr[right+1] - x):
                left -= 1
            else:
                right += 1

        return arr[left:right+1]

    def binary_search(self, arr, x):
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if arr[mid] < x:
                l = mid
            elif arr[mid] > x:
                r = mid
            else:
                return mid

        if abs(arr[l] - x) <= abs(arr[r] - x):
            return l
        else:
            return r
# O(k + logn) time, O(1) space
