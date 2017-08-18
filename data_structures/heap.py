from __future__ import print_function

# a priority queue is an abstract data type
# a heap is a data structure implementing priority queue
# a heap is a complete binary tree
# in a min-heap, values in each level is smaller values in next level

# swap an element with its parent / smallest children is guaranteed to keep a valid heap
# run sift_down() on half of the array is guraranteed to heapify that array

# in heapq module, all methods are static (no class definition)

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
        self.sift_up(self.size -1)

    # remove the samllest element, O(logn)
    def extract(self):
        self.swap(0, -1)
        ele = self.store.pop()
        self.sift_down(0)
        return ele

    # time complexity O(klogk + (n-k)logk) = O(nlogk)
    # same idea for k smallest elements
    @classmethod
    def k_largest(cls, arr, k):
        if k <= 0:
            return []
        if k > len(arr):
            return cls.heap_sort(arr, key=lambda x: -x)
        # start with an empty min-heap
        heap = cls()
        for i in range(k):
            heap.push(arr.pop())
        while len(arr) > 0:
            heap.push(arr.pop())
            heap.extract()
        return heap.store

    @classmethod
    def heapify(cls, arr, key=lambda x: x):
        heap = cls(arr, key)
        i = len(arr) // 2
        while i > 0:
            heap.sift_down(i)
            i -= 1
        return heap

    # stable, worst case time complexity O(nlogn), space complexity O(1)
    @classmethod
    def heap_sort(cls, arr, key=lambda x: x):
        # reverse the key since we need max-heapify later
        heap = cls(arr, lambda x: -key(x))
        # max-heapify within a range of 0 to 1, 2 ... n-1
        for i in range(1, len(arr)):
            heap.sift_down(0, i)
        # swap the first and last element within a range of 0 to n-1, n-2 ... 1
        for j in range(len(arr) - 1, 0, -1):
            heap.swap(0, j)
            # max-heapify each time after swapping
            heap.sift_up(j - 1)
        return heap.store

    # helper methods
    def cmp(self, i, j):
        x, y = self.store[i], self.store[j]
        # gt: 1, eq: 0, lt: -1
        return (self.key(x) > self.key(y)) - (self.key(x) < self.key(y))

    def swap(self, i, j):
        self.store[i], self.store[j] = self.store[j], self.store[i]

    # if parent_idx = n, child_indices = [2n+1, 2n+2]
    def smaller_child_index(self, i):
        left, right = i * 2 + 1, i * 2 + 2
        if right > len(self):
            return left
        elif self.cmp(left, right) < 0:
            return left
        else:
            return right

    def sift_up(self, child_idx):
        parent_idx = (child_idx - 1) // 2
        while parent_idx > 0:
            if self.cmp(parent_idx, child_idx) < 0:
                self.swap(child_idx, parent_idx)
            child_idx = parent_idx
            parent_idx = (parent_idx - 1) // 2

    def sift_down(self, parent_idx， end=len(self)):
        # while parent has at least one child
        while parent_idx * 2 + 1 < end:
            child_idx = self.smaller_child_index(parent_idx)
            if self.cmp(parent_idx, child_idx) > 0:
                self.swap(parent_idx, child_idx)
            parent_idx = child_idx



if __name__ == '__main__':
    heap = Heap.heapify([1, 5, 2, 4, 3])
    print(heap)

    arr = Heap.heap_sort([1, 5, 2, 4, 3])
    print(arr)

    arr_with_dup = Heap.heap_sort([3, 2, 2, 3, 1, 4])
    print(heap_with_dup)

    arr_with_attr = Heap.heap_sort([(0, 3), (1, 1), (2, 4)], key=lambda x: x[1])
    print(arr_with_attr)
