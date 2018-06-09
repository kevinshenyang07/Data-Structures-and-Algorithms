# Largest Rectangle in Histogram
def largest_rect_area(heights):
    heights.append(0)  # ensure the stack is cleared in the end
    stack = [-1]  # increasing stack
    max_area = 0
    for i in range(len(heights)):
        while heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]  # must be max height looking left
            w = i - 1 - stack[-1]  # when look left on (i-1)th bar, the max width that has height h
            max_area = max(max_area, h * w)
        stack.append(i)
    heights.pop()
    return max_area


#
# Next Greater Element Series

# find_nums = [4, 1, 2], nums = [1, 3, 4, 2]
# result = [-1, 3, -1] (array not circular)
def next_greater_element_1(find_nums, nums):
    next_greater = {}
    stack = []  # decreasing stack

    for num in nums:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    for num in stack:
        next_greater[num] = -1

    return [next_greater[n] for n in findNums]


# nums = [3, 1, 2, 1], result = [-1, 2, 3, 3] (array is circular)
def next_greater_element_2(nums):
    ans = [-1] * len(nums)
    stack = []

    for i in range(len(nums)) + range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = nums[i]
        stack.append(i)
    return ans


# find the smallest 32-bit integer that has the same digits and greater than n
# n = 12, result = 21
# n = 21, result = -1
def next_greater_element_3(n):
    # similar to next permutation
    digits = [d for d in str(n)]

    # 1. from right to left find the digit that is not greater than its next digit
    i = len(digits) - 1
    while i > 0 and digits[i-1] >= digits[i]:
        i -= 1

    if i == 0:
        return -1

    # 2. find the smallest digit that is greater than digits[i-1], then swap
    # i is now the start of dereasing sequence
    j = i
    while j < len(digits) and digits[i-1] < digits[j]:
        j += 1
    digits[i-1], digits[j-1] = digits[j-1], digits[i-1]  # digits[j-1] is the target digit

    # 3. reverse the new decreasing sequence
    j = len(digits) - 1
    while i < j:
        digits[i], digits[j] = digits[j], digits[i]
        i += 1
        j -= 1

    val = int(''.join(digits))
    return val if val <= 2 ** 31 - 1 else -1


if __name__ == '__main__':
    largest_rect_area([1, 3, 2, 4, 3, 5])