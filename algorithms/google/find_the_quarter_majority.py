# given a sorted array of n numbers, return any number with occurrences > n/4 times
# assume there'll be at lease one valid num, do better than O(n)
# sorted => binary search, appears more than n/4 => candidates must be at n/4, n/2 or n * 3/4
def find_quarter_majority(nums):
    if not any(nums):
        raise ValueError('input array is empty')

    n = len(nums)
    window = n / 4

    for k in range(1, 4):
        i = window * k
        left = bisect_first(nums, nums[i], i - n / 4, i)
        right = bisect_last(nums, nums[i], i, i + n / 4)
        if right - left + 1 > k:
            return nums[i]

    raise ValueError('no quarter majority')

def bisect_first(nums, target, left, right):
    while left + 1 < right:
        mid = left + (right - left) / 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    if nums[left] == target:
        return left
    return right

def bisect_last(nums, target, left, right):
    while left + 1 < right:
        mid = left + (right - left) / 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid
    if nums[right] == target:
        return right
    return left

if __name__ == '__main__':
    nums = [2,5,5,5,6,6,8,9,9,9]
    print bisect_first(nums, 5, 0, 10)
    print bisect_last(nums, 5, 0, 10)
    print find_quarter_majority(nums)
