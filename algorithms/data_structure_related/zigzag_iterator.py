from collections import deque

# Zigzag Iterator
# Given two 1d vectors, implement an iterator to return their elements alternately.
# v1 = [1,2], v2 = [3,4,5,6], f(v1, v2) => [1,3,2,4,5,6]
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = deque()
        if v1: self.queue.append((v1, 0))
        if v2: self.queue.append((v2, 0))

    def next(self):
        vec, i = self.queue.popleft()
        val = vec[i]
        if i < len(vec) - 1:
            self.queue.append((vec, i + 1))
        return val

    def has_next(self):
        return self.queue
# followup: there're k vectors instead of 2
