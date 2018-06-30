# any problem involving partition / swapping
def partition(nums, start, end):
    # if using random init pivot, swap to the left anyway
    pivot_val = nums[start]
    left = start + 1
    right = end
    # let right cross left to make sure nums[right] < pivot_val in the end
    # left equal to right covers the two elements situation
    while left <= right:
        if nums[left] <= pivot_val:
            left += 1
        elif nums[right] >= pivot_val:
            right -= 1
        # if two pointers haven't crossed yet and ready to swap
        else:
            nums[left], nums[right] = nums[right], nums[left]
    # swap pivot with the rightmost element that is smaller than pivot
    nums[start], nums[right] = nums[right], nums[start]
    return right
