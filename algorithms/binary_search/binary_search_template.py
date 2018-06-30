# 二分法：保留有解的那一半

# sorted array, no duplicates
# extra code so that it can also be used in finding leftmost target
# when there are duplicates
def binary_search(nums, target):
    if not nums:
        return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:  # start < end could get into infinite loop
        mid = start + (end - start) // 2  # prevent int overflow
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid
        else:
            end = mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1
