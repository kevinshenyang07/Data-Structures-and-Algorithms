# if an element is 0, set its entire row and col to 0
def set_zeros(matrix):
    m, n = len(matrix), len(matrix[0])
    # record the state before the row is marked
    first_row_has_zero = not all(matrix[0])
    # first row/col as marker
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # set zeros
    for i in range(1, m):
        for j in range(n - 1, -1, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # update the first row
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0


# Longest Palindrome Substring
def longest_palindrome(s):
    max_length = 0
    l = r = 0
    for i in range(len(s) - 1):
        # get palindromes of odd or even length
        l1, r1 = expand_palindrome(s, i, i)
        l2, r2 = expand_palindrome(s, i, i + 1)
        # update longest palindrome
        if r1 - l1 + 1 > max_length:
            max_length = r1 - l1 + 1
            l, r = l1, r1
        if r2 - l2 + 1 > max_length:
            max_length = r2 - l2 + 1
            l, r = l2, r2
    return s[l:r+1]


def expand_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return l + 1, r - 1


def longest_common_prefix(strs):
    if not strs:
        return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    for i in range(len(first)):
        if i >= len(last) or first[i] != last[i]:
            return first[:i]
    return first
# O(mnlogn) time, where m is the avg string length, n is the number of strings
# usually pretty fast because string comparsion may stop early


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


# Merge Intervals
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda inter: inter.start)
    merged = []
    for inter in intervals:
        # list out three situations:
        # 1. merged is empty => append interval
        # 2. merged is not empty, last.end < inter.start => append interval
        # 3. merged is not empty, last.end >= inter.start => update last.end
        if merged and merged[-1].end >= inter.start:
            merged[-1].end = max(merged[-1].end, inter.end)
        else:
            merged.append(inter)
    return merged


# Majority Number
# find the number that occurs more than half of the size of the array
# follow up: find number(s) occurs more than 1/3 of the size of the array
#         => have two candidates
def majority_element(nums):
    # if there is a majority number, that number is guaranteed to
    # have a positive counter in the end
    if not nums:
        return None
    # if counter is 0 or reduced to 0, update the candidate
    candidate = nums[0]
    counter = 0
    for num in nums:
        if counter == 0:
            candidate = num
        elif num == candidate:
            counter += 1
        else:
            counter -= 1
    # in [1,2,3,4], there will be no majority number
    # thus 2nd pass to double check
    counter = 0
    for num in nums:
        if num == candidate:
            counter += 1
    if counter <= (len(nums) + 1) // 2:
        return None
    else:
        return candidate


# Gas Station
# approach:
# 1. prove that if total gas is more than total cost, there must be a solution.
#    (for the station that has greatest negative diff, there must be one or more
#    stations that have a total positive balance greater than that negative dff)
# 2. find the point where the balance is lowest, the next index must be solution.
def can_complete_circuit(gas, cost):
    if len(gas) != len(cost) or sum(gas) < sum(cost):
        return -1
    position = 0
    balance = 0  # current tank balance
    for i in range(len(gas)):
        balance += gas[i] - cost[i]  # update balance
        if balance < 0:  # balance drops to negative, reset the start position
            balance = 0
            position = i + 1
    return position

