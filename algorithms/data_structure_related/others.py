# Contains Duplicate II
# high freq
def contains_duplicate(self, nums, k):
    window = set([])

    for i, num in enumerate(nums):
        if i > k:
            window.remove(nums[i-k-1])
        if num in window:
            return True
        window.add(num)

    return False
# O(n) time, O(k) space
# O(n) time and space if using hash table


def nth_ugly_number(n):
    # ugly[i2] means the largest base to be multiplied by 2
    # for example, the ugly numbers are [1, 2, 3, 4...]
    # candidates of ugly numbers must be left-right or top-down:
    # 1x2 2x2 3x2 4x2
    # 1x3 2x3 3x3 4x3
    # 1x5 2x5 3x5 4x5
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]:
            i2 += 1
        while ugly[i3] * 3 <= ugly[-1]:
            i3 += 1
        while ugly[i5] * 5 <= ugly[-1]:
            i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        # print(ugly)
    return ugly[-1]
# O(n) time, O(n) space


def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        # only check num from smallest num of sequence
        # range from [num, right)
        if num - 1 not in num_set:
            right = num + 1
            while right in num_set:
                right += 1
            max_length = max(max_length, right - num)
    return max_length
# O(n+L) time, O(n) space, L is the length of the sequence


if __name__ == '__main__':
    print nth_ugly_number(10)
