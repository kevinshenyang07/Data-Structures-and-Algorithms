from __future__ import print_function

# a priority queue is an abstract data type
# a heap is a data structure implementing priority queue
# a heap is a complete binary tree
# in a min-heap, values in each level is smaller values in next level

# swap an element with its parent / smallest children is guaranteed to keep a valid heap

class MinHeap(object):
    def __init__(self):

    def peek(self):

    # O(logn)
    def insert(self, ele):

    # remove the samllest element, O(logn)
    def extract(self):

    # max-heapify from left to right, then extract from right to left
    # stable, worst case time complexity O(nlogn), space complexity O(1)
    def heap_sort(self):
