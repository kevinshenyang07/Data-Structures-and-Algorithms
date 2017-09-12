# two pass version: count the number of each color, then set the colors
# O(n) time, O(k) space (k colors)

# more than one pass
def sort_colors(nums):
    # partition color 0 with color 1, 2
    split1 = partition(nums, 0, len(nums) - 1, 0)
    # partition color 1 with color 2
    split2 = partition(nums, split1, len(nums) - 1, 1)


def partition(nums, l, r, color):
    while l <= r:
        if nums[l] == color:
            l += 1
        elif nums[r] != color:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    return l  # starting index of another color


# one pass version
def sort_colors_one_pass(nums):
    if not nums:
        return
    # p0: next position for 0, p2: next position for 2 (right to left)
    p0, p2 = 0, len(nums) - 1
    i = 0
    while i <= p2:
        if nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
            # since the value of nums[p2] is unknown
            # i is not added by 1 here
        elif nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
            i += 1
        else:
            i += 1
