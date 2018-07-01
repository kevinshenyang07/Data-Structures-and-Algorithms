# Next Permutation
# modify nums in place, don't return anything
def next_permutation(nums):
    # 1. find longest decreasing suffix
    # starting from the right side
    start = len(nums) - 1
    while nums[start - 1] >= nums[start] and start >= 1:
        start -= 1
    # simply reverse if it's sorted
    if start == 0:
        reverse(nums, 0, len(nums) - 1)
        return
    # 2. with pivot = start - 1, find successor = rightmost index that
    # is greater than pivot value, then swap pivot and successor element
    for i in range(len(nums) - 1, start - 1, -1):
        if nums[start - 1] < nums[i]:
            nums[start - 1], nums[i] = nums[i], nums[start - 1]
            break
    # 3. reverse the suffix
    reverse(nums, start, len(nums) - 1)

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
