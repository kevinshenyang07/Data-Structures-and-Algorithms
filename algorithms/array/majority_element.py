# Moore Voting

# Majority Element
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# assume at leat one element
class Solution(object):
    def majorityElement(self, nums):
        count, major_num = 0, nums[0]

        for num in nums:
            if num == major_num:
                count += 1
            elif count == 0:
                count, major_num = 1, num
            else:
                count -= 1

        return major_num


# Majority Element II
class Solution(object):
    def majorityElement(self, nums):
        if not nums: return []

        count1 = count2 = 0
        major1 = major2 = nums[0]

        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
            elif count1 == 0:
                count1, major1 = 1, num
            elif count2 == 0:
                count2, major2 = 1, num
            else:
                count1 -= 1
                count2 -= 1

        res = []
        if nums.count(major1) > len(nums) / 3:
            res.append(major1)
        if major2 != major1 and nums.count(major2) > len(nums) / 3:
            res.append(major2)
        return res
