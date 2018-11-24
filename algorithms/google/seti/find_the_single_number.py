# given an array with pairs (each pair's elements are adjacent)
# with only one number that is not a pair, find that number
def find_single(nums):
    if not nums:
        return -1
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1

    while left + 2 < right:
        mid = left + (right - left) / 2

        if mid % 2 == 1:
            if nums[mid - 1] == nums[mid]:
                left = mid
            else:
                right = mid
        else:
            if nums[mid] == nums[mid + 1]:
                left = mid
            else:
                right = mid

    if nums[left] == nums[left + 1]:
        return right
    elif nums[left + 1] == nums[right]:
        return left
    return left + 1  # single number in the middle of two pairs


def test():
    print find_single([])  # -1
    print find_single([1])  # 0
    print find_single([1,1,3,5,5])  # 2
    print find_single([1,1,3,3,5])  # 4
    print find_single([1,1,3,3,4,4,5])  # 6
    print find_single([1,1,5,3,3,4,4])  # 2

if __name__ == '__main__':
    test()
