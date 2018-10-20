from heapq import heappush, heappop

# heap with key
class Heap(object):
    def __init__(self, key=lambda x: x):
        self.key = key
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, x):
        heappush(self.data, (self.key(x), x))

    def pop(self):
        return heappop(self.data)[1]

    # optional
    def peek(self):
        if self.data:
            return self.data[0][1]
