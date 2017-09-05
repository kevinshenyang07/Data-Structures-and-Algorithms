def longest_palindrome(s):
    palindrome = ''
    for i in range(len(s)):
        # get a palindrome of odd length
        palindrome_odd = expand_palindrome(s, i, i)
        if len(palindrome_odd) > len(palindrome):
            palindrome = palindrome_odd
        # get a palindrome of even length
        palindrome_even = expand_palindrome(s, i, i + 1)
        if len(palindrome_even) > len(palindrome):
            palindrome = palindrome_even
    return palindrome


def expand_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


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
