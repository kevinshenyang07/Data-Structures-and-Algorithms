# a priority queue is an abstract data type
# a heap is a data structure implementing priority queue
# a heap is a complete binary tree

# properties:
# in a min-heap, each child is smaller than or equal to its parent
# swap an element with its parent / smallest children is guaranteed to keep a valid heap
# run sift_down() on half of the array is guraranteed to heapify that array

class Heap(object):

    def __init__(self, key=lambda x: x):
        self.store = []
        self.key = key

    def __len__(self):
        return len(self.store)

    def is_empty(self):
        return not self.store

    def peek(self):
        if len(self) == 0:
            raise IndexError("heap index out of range")
        return self.store[0]

    # O(logn)
    def push(self, ele):
        self.store.append(ele)
        self.sift_up(len(self) - 1)

    # remove the samllest element, O(logn)
    def pop(self):
        self.swap(0, -1)
        ele = self.store.pop()
        self.sift_down(0)
        return ele

    def sift_up(self, child_idx):
        while child_idx > 0:
            parent_idx = (child_idx - 1) // 2

            if self.cmp(parent_idx, child_idx) > 0:
                self.swap(parent_idx, child_idx)

            child_idx = parent_idx

    def sift_down(self, parent_idx):
        # while parent has at least one child
        while parent_idx * 2 + 1 < len(self):
            child_idx = self.smaller_child_index(parent_idx)
            if self.cmp(parent_idx, child_idx) > 0:
                self.swap(parent_idx, child_idx)
            parent_idx = child_idx

    def smaller_child_index(self, i):
        left, right = i * 2 + 1, i * 2 + 2

        if right >= len(self):
            return left
        elif self.cmp(left, right) <= 0:
            return left
        else:
            return right

    def cmp(self, i, j):
        x, y = self.store[i], self.store[j]
        if self.key(x) < self.key(y):
            return -1
        if self.key(x) > self.key(y):
            return 1
        return 0

    def swap(self, i, j):
        self.store[i], self.store[j] = self.store[j], self.store[i]


if __name__ == '__main__':
    pq = Heap(key=lambda x: -x)
    for num in [3,2,2,1,4,5,2]:
        pq.push(num)

    print pq.peek()

    while not pq.is_empty():
        print pq.pop()

