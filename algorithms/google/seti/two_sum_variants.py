# two sum that is closest to target, returns the min diff
def two_sum_closest(nums, target):
    if not nums or len(nums) < 2:
        raise ValueError()

    nums.sort()
    i, j = 0, len(nums) - 1
    min_diff = float('inf')

    while i < j:
        curr_diff = nums[i] + nums[j] - target
        min_diff = min(min_diff, abs(curr_diff))

        if curr_diff < 0:
            i += 1
        else:
            j -= 1

    return min_diff
# test cases
# [], 5 => ValueError
# [1], 5 => ValueError
# [1,2], 5 => [1,2]
# [-3,2,1], 5 => [1,2]

# find number of pairs that has sum greater than target
def two_sum_larger_than(nums, target):
    nums.sort()
    i, j = 0, len(nums) - 1
    num_pairs = 0

    while i < j:
        curr_sum = nums[i] + nums[j]
        if curr_sum <= target:
            i += 1
        else:
            num_pairs += j - i
            j -= 1

    return num_pairs
# test cases
# [], 5 => 0
# [1], 5 => 0
# [1,6], 5 => 1
# [1,3,5,7], 5 => 5

if __name__ == '__main__':
    print two_sum_larger_than([1,3,5,7], 5)
