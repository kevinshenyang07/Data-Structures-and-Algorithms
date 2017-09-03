from __future__ import print_function
import heapq


# Java API
# PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
# pq.add(1)  // push
# pq.peek()
# pq.poll()  // extract


# Valid Parentheses
def is_valid(s):
    

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


if __name__ == '__main__':
    nth_ugly_number(10)
