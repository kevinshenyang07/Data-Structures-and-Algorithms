# Search in Rotated Sorted Array
# assume no duplicates
def search_rotated(nums, target):
    if not nums:  # empty list or None
        return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:  # make sure start and mid don't meet
        mid = start + (end - start) // 2
        # two cases * two conditions
        if nums[mid] == target:
            return mid
        if nums[start] < nums[mid]:  # mid is on the left half
            # find the condition that divide possible solution range
            if nums[start] <= target <= nums[mid]:
                end = mid
            else:  # other wise cut from start to mid
                start = mid
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid
            else:
                end = mid
    # handle the cases when start = mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1
