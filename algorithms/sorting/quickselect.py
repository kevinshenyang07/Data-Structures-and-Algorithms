def find_kth_largest(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return 0
    return select(nums, 0, len(nums) - 1, len(nums) - k)


def select(nums, left, right ,k):
    if left == right:
        return nums[left]
    pivot = partition(nums, left, right)
    if pivot == k:
        return nums[pivot]
    elif pivot < k:
        return select(nums, pivot + 1, right, k)
    else:
        return select(nums, left, pivot - 1, k)


def partition(nums, left, right):
    pivot_val = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot_val:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot_val:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot_val
    return left


# O(n) time, O(n^2) worst case, O(1) space
