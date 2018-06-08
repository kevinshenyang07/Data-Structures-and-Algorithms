from __future__ import print_function
from collections import deque


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


# assumption: array is not empty, 1 <= k <= len(nums)
def max_sliding_window(nums, k):
    # monotonic decreasing deque of elements's indices
    result = []
    dq = []
    for i in range(len(nums)):
        # remove index if out of the windex [i-(k-1), i]
        if dq and dq[0] < i - k + 1:
            dq.pop(0)
        # remove indices whose element is smallers than nums[i]
        # since they don't have chance to be max any more
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        # now i guaranteed to be smallest
        dq.append(i)
        # start adding to result from index k - 1
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


# Largest Rectangle in Histogram
def largest_rect_area(heights):
    heights.append(0)  # ensure the stack is cleared in the end
    stack = [-1]  # monotonous stack
    max_area = 0
    for i in range(len(heights)):
        while heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]  # must be max height looking left
            w = i - 1 - stack[-1]  # when look left on (i-1)th bar, the max width that has height h
            max_area = max(max_area, h * w)
        stack.append(i)
    heights.pop()
    return max_area


# Implement Stack using Queues
class QueueStack(object):
    def __init__(self):
        self._queue = deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()


if __name__ == '__main__':
    nth_ugly_number(10)