from __future__ import print_function
import collections
import heapq


# Java API
# PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
# pq.add(1)  // push
# pq.peek()
# pq.poll()  // extract


def nth_ugly_number_pq(n):
    if n == 1:
        return 1
    pq = [1]
    for i in range(1, n):
        minimum = heapq.heappop(pq)
        while pq and pq[0] == minimum:
            heapq.heappop(pq)
        heapq.heappush(pq, minimum * 2)
        heapq.heappush(pq, minimum * 3)
        heapq.heappush(pq, minimum * 5)
        # print(pq)
    return pq[0]
# O(nlogn) time, O(n) space


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
    # using monotonic deque of indices, of which elements
    # order form large to small
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


# trapping rain water
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) <= 2:
        return 0
    vol = 0
    highest = [0] * len(height)
    # max height looking left, both ends cannot contain water
    for i in range(1, len(height) - 1):
        highest[i] = max(highest[i - 1], height[i - 1])
    # update if max height looking right is lower than max height looking left
    for j in range(len(height) - 2, -1, -1):
        highest[j] = min(highest[j], max(highest[j + 1], height[j + 1]))
    # vol trapped on each slot
    for k in range(1, len(height) - 1):
        if highest[k] > height[k]:
            vol += highest[k] - height[k]
    return vol
# O(n) time and space


# find median in a stream
class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        max_pq, min_pq = self.heaps
        # push to min_pq, get the minimum, then push to max_pq
        heapq.heappush(min_pq, num)
        ele = heapq.heappop(min_pq)
        heapq.heappush(max_pq, -ele)
        # keep the balance between max_pq and min_pq
        if len(max_pq) > len(min_pq):
            # move one ele from max_pq to min_pq
            ele = heapq.heappop(max_pq)
            heapq.heappush(min_pq, -ele)

    def findMedian(self):
        max_pq, min_pq = self.heaps
        if len(max_pq) < len(min_pq):
            return float(min_pq[0])
        return (min_pq[0] - max_pq[0]) / 2.0


# Implement Stack using Queues
class QueueStack(object):
    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()


if __name__ == '__main__':
    nth_ugly_number(10)
