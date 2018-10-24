# Maximum Subarray
def max_subarray(nums):
    if not nums:
        return 0
    curr_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        # if curr_sum + nums[i] < 0, have a new start, otherwise accumulate
        curr_sum = max(curr_sum + nums[i], nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum


# Maximum Product Subarray
# the array has at least one number
def max_product_subarray(nums):
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

