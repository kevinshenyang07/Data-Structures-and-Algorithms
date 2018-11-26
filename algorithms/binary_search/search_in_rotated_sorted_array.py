# Search in Rotated Sorted Array
# assume no duplicates
def search_rotated(nums, target):
    if not nums: return -1

    left, right = 0, len(nums) - 1

    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        # if there're duplicates:
        # while left < mid and nums[left] == nums[mid]:
        #     left += 1
        # length of rotated part < (right - left) / 2
        if nums[left] < nums[mid]:
            # continuous range on the left
            if nums[left] <= target <= nums[mid]:
                right = mid
            else:
                left = mid
        else:
            # continuous range on the right
            if nums[mid] <= target <= nums[right]:
                left = mid
            else:
                right = mid
    # handle boundary cases
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1

