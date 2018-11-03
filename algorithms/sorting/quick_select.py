# find kth largest = find (n-k)th smallest
def find_kth_largest(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return 0
    return quick_select(nums, 0, len(nums) - 1, len(nums) - k)

# find kth smallest in range
def quick_select(nums, i, j ,k):
    if i == j:
        return nums[i]

    pivot = partition(nums, i, j)
    # narrow the partition range by pivot index
    if pivot < k:
        return quick_select(nums, pivot + 1, j, k)
    elif pivot > k:
        return quick_select(nums, i, pivot - 1, k)
    else:
        return nums[pivot]

# partition with two pointers, returns a partition index where
# every element on the left is <= nums[i] (pivot value)
# every element on the right is >= nums[i]
def partition(nums, i, j):
    # if using random init pivot, swap to the left anyway
    left = i + 1
    right = j
    # let right cross left to make sure nums[right] < nums[i] in the end
    # left equal to right covers the two elements situation
    while left <= right:
        if nums[left] <= nums[i]:
            left += 1
        elif nums[right] >= nums[i]:
            right -= 1
        # if two pointers haven't crossed yet and ready to swap
        else:
            nums[left], nums[right] = nums[right], nums[left]
    # swap pivot with the rightmost element that is smaller than pivot
    nums[i], nums[right] = nums[right], nums[i]
    return right
# O(n) time, O(n^2) worst case, O(1) space
# the first call of partition takes O(n), the next take an average of O(n/2)...
# worst case happens on selecting maximum on a sorted list, using 0 as pivot index

if __name__ == '__main__':
    nums = [10, 4, 5, 8, 6, 11, 26]
    print find_kth_largest(nums, 4)  # 8
