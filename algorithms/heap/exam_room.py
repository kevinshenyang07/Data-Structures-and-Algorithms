from heap import Heap

# Exam Room
# Assume ExamRoom.leave(p) are calls are valid.
class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.heap = Heap(lambda i: -self.distance(i))
        self.heap.push((-1, N))

    def seat(self):
        """
        :rtype: int
        """
        start, end = self.heap.pop()

        if start == -1:
            self.heap.push((0, end))
            return 0
        if end == self.N:
            self.heap.push((start, self.N - 1))
            return self.N - 1

        mid = (start + end) / 2
        self.heap.push((start, mid))
        self.heap.push((mid, end))
        return mid

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        new_heap = Heap(lambda i: -self.distance(i))
        new_start, new_end = -1, self.N   # for the merged interval in the future

        while len(self.heap) > 0:
            interval = self.heap.pop()

            if p == interval[0]:
                new_end = interval[1]
            elif p == interval[1]:
                new_start = interval[0]
            else:
                new_heap.push(interval)

        new_heap.push((new_start, new_end))
        self.heap = new_heap

    # maximum new distance when a new student is seated
    def distance(self, interval):
        s, e = interval
        # open on start / end
        if s == -1:
            return e
        if e == self.N:
            return self.N - 1 - s

        return (e - s) / 2
# O(logn) for seat(), O(n) for leave(), which cna be reduced to O(logn) with hashmap
