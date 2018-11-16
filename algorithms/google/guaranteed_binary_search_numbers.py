# give a unsorted array with distinct numbers, find the counter of numbers { target1, target2, ...}
# which if we peform binary_search(nums, target), will returns the correct index
# approach:
# on each index i, if nums[i] > max(nums[:i]) and nums[i] < min(nums[i+1:]), add count
def guaranteed_binary_search_numbers(nums):
    if nums is None:
        return 0
    if len(nums) <= 1:
        return len(nums)

    n = len(nums)
    left_max = float('-inf')  # track left_max on the fly
    right_min = [float('inf')] * (n + 1)
    count = 0

    for i in range(n - 1, -1, -1):
        right_min[i] = min(right_min[i + 1], nums[i])

    for i in range(n):
        if left_max < nums[i] < right_min[i + 1]:
            count += 1
        left_max = max(left_max, nums[i])

    return count


if __name__ == '__main__':
    print guaranteed_binary_search_numbers([])  # 0
    print guaranteed_binary_search_numbers([1])  # 1
    print guaranteed_binary_search_numbers([1,2])  # 2
    print guaranteed_binary_search_numbers([2,1])  # 0
    print guaranteed_binary_search_numbers([2,1,3,4,5,6])  # 4
    print guaranteed_binary_search_numbers([2,1,3,4,6,5])  # 2
    print guaranteed_binary_search_numbers([2,1,3,5,4,6])  # 2
