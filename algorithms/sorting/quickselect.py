# partition with two pointers
def find_kth_largest(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return 0
    return select(nums, 0, len(nums) - 1, len(nums) - k)


def select(nums, left, right ,k):
    if left == right:
        return nums[left]

    pivot = partition(nums, left, right)
    
    # only partition the range that contains k
    if pivot == k:
        return nums[pivot]
    elif pivot < k:
        return select(nums, pivot + 1, right, k)
    else:
        return select(nums, left, pivot - 1, k)


def partition(nums, left, right):
    # if using random init pivot, switch to the left anyway
    pivot_val = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot_val:
            right -= 1
        # the smaller number take the init pivot's place
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot_val:
            left += 1
        # the bigger number move to the right side
        nums[right] = nums[left]
    # the pivot move to where it should be
    nums[left] = pivot_val
    return left


# O(n) time, O(n^2) worst case, O(1) space
# the first call of partition takes O(n), the next take an average of O(n/2)...
