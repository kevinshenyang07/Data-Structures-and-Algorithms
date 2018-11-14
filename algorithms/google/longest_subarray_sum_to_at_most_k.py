# assume numbers are non-negative
def longest_subarray_sum(nums, k):
    i = 0
    curr_sum = 0
    max_cnt = 0
    # [i, j] to be the window
    for j, num in enumerate(nums):
        curr_sum += num

        while i <= j and curr_sum > k:
            curr_sum -= nums[i]
            i += 1

        max_cnt = max(max_cnt, j - i + 1)
    return max_cnt

def test():
    print longest_subarray_sum([], 5)
    print longest_subarray_sum([10,2,2,3,1], 7)
    print longest_subarray_sum([1,2,3,99,1,2,3,4], 10)

if __name__ == '__main__':
    test()

