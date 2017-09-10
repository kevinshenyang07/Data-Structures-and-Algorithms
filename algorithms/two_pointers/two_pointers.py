# Two Sum approach: hashmap or sort + pointers
# Two Sum - Array is Sorted
def two_sum2(nums, target):
    start, end = 0, len(nums) - 1
    while start < end:
        if nums[start] + nums[end] == target:
            return [start + 1, end + 1]
        elif nums[start] + nums[end] < target:
            start += 1
        else:
            end -= 1
    return []
# O(n) time, O(1) space

    
# find element a, b, c that sum to 0, return unique combinations
def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        # if there are duplicates, move to the last one
        if i > 0 and nums[i-1] == nums[i]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum_of_three = nums[i] + nums[l] + nums[r]
            if sum_of_three < 0:
                l += 1
            elif sum_of_three > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                # skip the duplicates
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r-1] == nums[r]:
                    r -= 1
                l += 1; r -= 1
    return result
# O(n^2) time, O(1) space


# Merge Sorted Array
# assumption: nums1 has extra space to hold all the elements in nums
# m and n are the number of elements in these two static arrays
def merge(nums1, m, nums2, n):
    while m > 0:
        # starting from the right sides
        # index after m+n-1 to be the merged part
        if nums1[m - 1] < nums1[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
    # if n == 0 then the pointer has moved n times
    # else nums has n elements smaller than all nums1 elements
    if n > 0:
        for i in range(n):
            nums1[i] = nums2[i]


# Longest Substring Without Repeating Characters
# the substring has to be continuous
def length_of_longest_substring(s):
    start = max_length = 0
    char_idx = {}  # char: index that char last appeared

    for i in range(len(s)):
        # if there is a repeating char and it's within scope
        if s[i] in char_idx and start <= char_idx[s[i]]:
            # starting from the index after that repeating char
            start = char_idx[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        # update the index anyway
        char_idx[s[i]] = i

    return max_length


# Interleaving Positive and Negative Numbers
# for example, [-1,-2,-3,4,5,6] => [-1,4,-2,5,-3,6]
# do it in place without extra space
def rerange(nums):
    if len(nums) <= 1:
        return
    # find number of positive integers to 
    num_pos = 0
    for num in nums:
        if num >= 0:
            num_pos += 1
    # determine if the array should start with pos or neg number
    # initialize same-way pointers, if more pos numbers the pointer
    # must start from 0, otherwise will mess up the swapping
    if num_pos * 2 >= len(nums):
        pos, neg = 0, 1
    else:
        neg, pos = 1, 0
    # if either all pos numbers or all neg numbers are in their place,
    # then it's done, the rest are extra neg/pos numbers
    while pos < len(nums) and neg < len(nums):
        if nums[pos] >= 0:  # then the element is in its place
            pos += 2
        elif nums[neg] < 0:
            neg += 2
        else:
            nums[pos], nums[neg] = nums[neg], nums[pos]
# O(n) time, O(1) space    


# move zeros to the end of array, do it in-place
def move_zeros(nums):
    if len(nums) <= 1:
        return
    # find the initial index of zero
    p0 = 0
    while p0 < len(nums) and nums[p0] != 0:
        p0 += 1
    # start at the index after zero pointer
    for i in range(p0 + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            # nums[p0+1] is guaranteed to be 0
            p0 += 1


# Remove Duplicates from Sorted Array
# returns the length of deduplicated array
def remove_duplicates(nums):
    # 1 2 2 2 3
    # 1 2 3 2 3
    if not nums:
        return 0
    end = 0  # current end of deduplicated array
    for i in range(len(nums)):
        if nums[i] != nums[end]:
            end += 1
            nums[end] = nums[i]
    return end + 1


# Permutation in String
# assumption: input strings only contain lower case letters
def check_inclusion(s1, s2):
    # permutation of s1 in s2 => same counts of different chars
    # in a substring of s2 => sliding window
    if len(s1) > len(s2):
        return False
    # map a-z to 0-25
    A = [ord(char) - ord('a') for char in s1]
    B = [ord(char) - ord('a') for char in s2]
    # count for each letter, will be the diffences of counts 
    # between two strings
    counts = [0] * 26
    for x in A:
        counts[x] += 1

    for i, x in enumerate(B):
        # when a char moves in, update the count
        counts[x] -= 1
        if i >= len(A):
            # when a char moves out of the window, add the count back
            counts[B[i-len(A)]] += 1
        if all(c == 0 for c in counts):
            return True
    return False
