from __future__ import print_function


# a priority queue is an abstract data type
# a heap is a data structure implementing priority queue
# a heap is a complete binary tree

# properties:
# in a min-heap, each child is smaller than or equal to its parent
# swap an element with its parent / smallest children is guaranteed to keep a valid heap
# run sift_down() on half of the array is guraranteed to heapify that array

#
# heapq usage
from heapq import heapify, heappush, heappop
# initialize
arr = [1, 3, 2]
heapify(arr)  # in place, need to implement __cmp__ if other types
# or
pq = []
heappush(pq, 1)
heappop(pq)


# in-house implementation
class Heap(object):

    def __init__(self, store=[], key=lambda x: x):
        self.store = store
        self.key = key

    def __len__(self):
        # len() is O(1) since list objects keep counts inside
        return len(self.store)

    def peek(self):
        if len(self) == 0:
            raise IndexError("heap index out of range")
        return self.store[0]

    # O(logn)
    def push(self, ele):
        self.store.append(ele)
        self.sift_up(len(self) -1)

    # remove the samllest element, O(logn)
    def extract(self):
        self.swap(0, -1)
        ele = self.store.pop()
        self.sift_down(0)
        return ele

    @classmethod
    def k_largest(cls, arr, k):
        if k <= 0:
            return []
        if k > len(arr):
            return cls.heap_sort(arr, key=lambda x: -x)
        # start with an empty min-heap
        pq = cls()
        for i in range(k):
            pq.push(arr[i])
        for j in range(k, len(arr)) > 0:
            pq.push(arr[j])
            pq.extract()
        return pq.store
    # O(klogk + (n-k)logk) = O(nlogk) time, O(k) space
    # same idea for k smallest elements

    @classmethod
    def heapify(cls, arr, key=lambda x: x, end=None):
        if not end:
            end = len(arr)
        pq = cls(arr, key)
        i = end // 2
        while i >= 0:
            pq.sift_down(i, end)
            i -= 1
        return pq.store
    # time complexity O(nlogn)

    @classmethod
    def heap_sort(cls, arr, key=lambda x: x):
        # reverse the key to turn the array in max heap order
        _key = lambda x: -key(x)
        max_heap_arr = cls.heapify(arr, _key)
        # swap the biggest element to the end, then sift down the first element
        max_heap = cls(max_heap_arr, _key)
        for i in range(len(arr) - 1, 0, -1):
            max_heap.swap(0, i)
            max_heap.sift_down(0, i)
        return max_heap.store
    # stable, worst case time complexity O(nlogn), space complexity O(1)
    # sort result not stable (not guaranteed to reserve the original order)

    # helper methods
    def cmp(self, i, j):
        x, y = self.store[i], self.store[j]
        # gt: 1, eq: 0, lt: -1
        return (self.key(x) > self.key(y)) - (self.key(x) < self.key(y))

    def swap(self, i, j):
        self.store[i], self.store[j] = self.store[j], self.store[i]

    def smaller_child_index(self, i, end=None):
        if not end:
            end = len(self)
        # if parent_idx = n, child_indices = [2n+1, 2n+2]
        left, right = i * 2 + 1, i * 2 + 2
        if right >= end:
            return left
        elif self.cmp(left, right) < 0:
            return left
        else:
            return right

    def sift_up(self, child_idx):
        parent_idx = (child_idx - 1) // 2
        while parent_idx >= 0:
            if self.cmp(parent_idx, child_idx) < 0:
                self.swap(child_idx, parent_idx)
            child_idx = parent_idx
            parent_idx = (parent_idx - 1) // 2

    def sift_down(self, parent_idx, end=None):
        if not end:
            end = len(self)
        # while parent has at least one child
        while parent_idx * 2 + 1 < end:
            child_idx = self.smaller_child_index(parent_idx, end)
            if self.cmp(parent_idx, child_idx) > 0:
                self.swap(parent_idx, child_idx)
            parent_idx = child_idx


if __name__ == '__main__':
    pq = Heap.heapify([7, 5, 8, 2, 4, 3, 9, 1])
    print(pq)

    arr = Heap.heap_sort([7, 5, 8, 2, 4, 3, 9, 1])
    print(arr)

    arr_with_dup = Heap.heap_sort([7, 5, 3, 2, 4, 3, 5, 1])
    print(arr_with_dup)

    arr_with_attr = Heap.heap_sort([(0, 3), (1, 1), (2, 4)], key=lambda x: x[1])
    print(arr_with_attr)
