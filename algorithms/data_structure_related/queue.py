from collections import deque


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