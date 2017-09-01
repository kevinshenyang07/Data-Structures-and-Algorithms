def max_sub_array(nums):
    if not nums:
        return 0
    curr_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        # if curr_sum < 0, have a new start, otherwise accumulate
        curr_sum = max(num, curr_sum + num)
        max_sum = max(curr_sum, max_sum)
    return max_sum


# the array has at least one number
def max_prodcut_array(nums):
    res = pmax = pmin = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        # multiplied by a negative makes big number smaller
        if num < 0:
            pmax, pmin = pmin, pmax
        # either have a new start or further product
        pmax = max(num, pmax * num)
        pmin = min(num, pmin * num)
        # compare with global maximum
        res = max(res, pmax)

    return res
