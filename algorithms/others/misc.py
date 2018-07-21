# Set Matrix Zeros
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


# Sparse Matrix Multiplication
# assume A and B are valid matrix
def multiply(A, B):
    mA, nA, nB = len(A), len(A[0]), len(B[0])

    res = [[0] * nB for _ in range(mA)]

    for i in range(mA):
        for j in range(nA):
            if A[i][j]:
                # for row j in B, accumulate value of res[i][k]
                for k in range(nB):
                    res[i][k] += A[i][j] * B[j][k]
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
    counter = 1
    for i in range(1, len(nums)):
        if nums[i] == candidate:
            counter += 1
        else:
            counter -= 1
        # if count down to 0, assign current number as candidate
        if counter == 0:
            candidate = nums[i]
            counter = 1
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


def trailing_zeros(n):
    # count the number of 5s
    # all numbers contributing 5s are in a form of m * (5 ^ n)
    # so the total number of 5s are n / 5 + n / 25 + n / 125 ...
    # each 5 ^ 2 will provide an extra 5 for 5 ^ 1
    zeros = 0
    while n > 0:
        n = n // 5
        zeros += n
    return zeros


# Happy Numbers
def is_happy(n):
    # if it's not a happy number, the square sum will never
    # be 1 => find loop
    slow = digit_square_sum(n)
    fast = digit_square_sum(slow)
    while slow != fast:
        slow = digit_square_sum(slow)
        fast = digit_square_sum(fast)
        fast = digit_square_sum(fast)
    return slow == 1


def digit_square_sum(x):
    res = 0
    while x > 0:
        digit = x % 10
        res += digit ** 2
        x = x // 10
    return res


# Count the number of prime numbers less than a non-negative number, n.
def count_primes(n):
    if n <= 2:  # prime numbers start from 2
        return 0
    res = [True] * n
    res[0] = res[1] = False
    for i in range(2, n):
        if res[i] is True:
            # a multiplied prime number must not be prime
            for j in range(2, (n - 1) // i + 1):
                res[i * j] = False
    return sum(res)


# Sum of Two Integers
# 11 = 1011
# 6  =  110
# 11,6 => 13,4 => 9,8 => 1,16 => 17,0
def get_sum(a, b):
    if a == 0 or b == 0:
        return a or b
    while b != 0:
        carry = a & b  # digits that add up to 2
        a = a ^ b  # digits that add up to 1 or 0
        b = carry << 1
    return a
# recursive:
# get_sum(a, b) = get_sum(a ^ b, (a & b) << 1)
# base case: get_sum(a, 0) == a


# Valid Triangle Number
# assumption: nums[i] > 0
# sort and count the number of triplets at indices x < y < z
# such that len_x + len_y > len_z
def triangle_number(nums):
    nums.sort()
    result = 0
    for x in range(len(nums)):
        z = x + 2
        for y in range(x + 1, len(nums)):
            while z < len(nums) and nums[x] + nums[y] > nums[z]:
                z += 1
            result += z - y - 1
    return result
# O(n^2) time, O(1) space

# Find Celebrity
# celebrity: one that everybody knows but knows nobody
# represent people from 0 to n - 1
# offers api #knows(a, b), returns True if a knows b
def find_celebrity:
    candidate = 0
    # if knows(a, b), a must not be a celebrity
    # if not knows(a, b), b must not be a celebrity
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    # check if candidate is valid
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate
# O(n) time
# O(n ^ 2) time for brute force
