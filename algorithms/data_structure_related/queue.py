from collections import deque


# assumption: array is not empty, 1 <= k <= len(nums)
def max_sliding_window(nums, k):
    result = []
    dq = []  # decreasing deque
    for i, num in enumerate(nums):
        # add num to the deque
        # since num is the newest element, elements in deque that are
        # smaller than num won't have a chance to be window maximum
        while dq and dq[-1] < num:
            dq.pop()
        dq.append(num)

        # move nums[i-k] out of window
        # nums[i-k] < dq[0] not possible since it would have been poped out when dq[0] comes in
        # nums[i-k] > dq[0] not possible since it would take the place of dq[0]
        if i >= k and nums[i-k] == dq[0]:
            dq.pop(0)

        # start adding to result from index k - 1
        if i >= k - 1:
            result.append(dq[0])
    return result
# O(n) time and space


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