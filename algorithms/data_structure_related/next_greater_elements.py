# increasing stack to find the next smaller element (for each element)
# decreasing stack to find the next greater element

# Next Greater Element I
# find_nums = [4, 1, 2], nums = [1, 3, 4, 2]
# result = [-1, 3, -1] (array not circular)
class Solution(object):
    def nextGreaterElement(find_nums, nums):
        next_greater = {}
        stack = []  # decreasing stack

        for num in nums:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        return [next_greater[n] for n in findNums]


# Next Greater Element II
# nums = [3, 1, 2, 1], result = [-1, 2, 3, 3] (array is circular)
class Solution(object):
    def nextGreaterElements(self, nums):
        ans = [-1] * len(nums)
        stack = []

        for i in range(len(nums)) + range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans


# Next Greater Element III
# find the smallest 32-bit integer that has the same digits and greater than n
# n = 12, result = 21
# n = 21, result = -1
class Solution(object):
    def nextGreaterElement(self, n):
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
        return val if val <= float('inf') else -1
