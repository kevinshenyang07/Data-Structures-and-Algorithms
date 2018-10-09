# find kth largest = find (n-k)th smallest
def find_kth_largest(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return 0
    return select(nums, 0, len(nums) - 1, len(nums) - k)

# find kth smallest in range
def select(nums, start, end ,k):
    if start == end:
        return nums[start]

    pivot = partition(nums, start, end)
    # only partition the range that contains k
    if pivot == k:
        return nums[pivot]
    elif pivot < k:
        return select(nums, pivot + 1, end, k)
    else:
        return select(nums, start, pivot - 1, k)

# partition with two pointers, returns a partition index where
# every element on the left is <= nums[i]
# every element on the right is >= nums[i]
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


# O(n) time, O(n^2) worst case, O(1) space
# the first call of partition takes O(n), the next take an average of O(n/2)...
# worst case happens on selecting maximum on a sorted list, using 0 as pivot index
