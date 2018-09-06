# 二分法：保留有解的那一半

# sorted array, no duplicates
# extra code so that it can also be used in finding leftmost target
# when there are duplicates
def binary_search(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:  # left < right could get into infinite loop
        mid = left + (right - left) // 2  # prevent int overflow
        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            return mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1
