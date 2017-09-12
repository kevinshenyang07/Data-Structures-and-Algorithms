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


# things to handle:
# surrounding whitespace chars
# + or - sign
# letters following digits can be ignored
# integer should be within int range
# return 0 for invalid input
def my_atoi(s):
    s = s.strip()
    if len(s) == 0:
        return 0
    chars = list(s)

    sign = -1 if chars[0] == '-' else 1
    if chars[0] in ['+', '-']:
        del chars[0]
    
    res, i = 0, 0
    digits = '0123456789'
    while i < len(chars) and chars[i] in digits:
        res = res * 10 + digits.index(chars[i])
        i += 1
    
    # return val in the range of [INT_MIN, INT_MAX]
    return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


# Valid Number
def is_numeric(s):
    # define a DFA
    # type of char => state
    state = [{},
            {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
            {'digit': 3, '.': 4},
            {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
            {'digit': 5},
            {'digit': 5, 'e': 6, 'blank': 9},
            {'sign': 7, 'digit': 8},
            {'digit': 8},
            {'digit': 8, 'blank': 9},
            {'blank': 9}]
    current_state = 1
    # recognize the type of each char
    for c in s:
        if c >= '0' and c <= '9':
            c = 'digit'
        if c == ' ':
            c = 'blank'
        if c in ['+', '-']:
            c = 'sign'
        if c not in state[current_state].keys():
            return False
        # jump to a new state
        current_state = state[current_state][c]
    # is numeric only if the final state is in the following
    if current_state not in [3, 5, 8, 9]:
        return False
    return True


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


# Roman Numeral
# I: 1, V:5, X:10, L: 50, C: 100, D: 500, M: 1000
# only one char is allowed to put on the left to represent subtration

# Roman to Integer
# the range of the value is [1, 4000)
def roman_to_int(s):
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50,
               "C": 100, "D": 500, "M": 1000}
    res = 0
    for i, c in enumerate(s):
        if i < len(s) - 1 and mapping[s[i]] < mapping[s[i + 1]]:
            res -= mapping[s[i]]
        else:
            res += mapping[s[i]]
    return res


# Integer to Roman
# the range of the value is [1, 4000)
def int_to_roman(num):
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10]
