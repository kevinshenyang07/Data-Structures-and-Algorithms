class DynamicArray(object):
    # capacity starts with 8
    def __init__(self):
        self.capacity = 8
        self.store = [None] * self.capacity
        self.length = 0
        self.start_idx = 0

    # O(1) for arr[i]
    def __getitem__(self, i):
        i = self.get_index(i)
        return self.store[i]

    # O(1) for arr[i] = x
    def __setitem__(self, i, val):
        i = self.get_index(i)
        self.store[i] = val

    # O(1) for del arr[i]
    def __delitem__(self, i):
        i = self.get_index(i)
        self.store[i] = None

    def __repr__(self):
        return self.store.__repr__()

    # O(1)
    def pop(self):
        if self.length == 0:
            raise ValueError("pop from empty array")
        else:
            ele = self.store[self.length-1]
            self.store[self.length-1] = None
            self.length -= 1
            return ele

    # O(1)
    def push(self, ele):
        if self.length == self.capacity:
            self.resize()
        self[self.length] = ele
        self.length += 1

    # O(1) using ring buffer
    def shift(self):
        if self.length == 0:
            raise ValueError("shift from empty array")
        else:
            first, self[0] = self[0], None
            self.start_idx = (self.start_idx + 1) % self.capacity
            self.length -= 1
            return first

    # O(1) using ring buffer
    def unshift(self, ele):
        if self.length == self.capacity:
            self.resize()
        self.start_idx = (self.start_idx - 1) % self.capacity
        self[0] = ele
        self.length += 1

    #
    def get_index(self, i):
        if i < 0 or i > self.length:
            raise IndexError
        else:
            return (self.start_idx + i) % self.capacity

    def resize(self):
        # new size = 1.5 * old size + 6
        new_capacity = self.capacity * 2
        new_store = [None] * new_capacity

        # copy the data to new store
        for i in range(self.length):
            new_store[i] = self[i]
        self.store = new_store
        self.capacity = new_capacity
        self.start_idx = 0
