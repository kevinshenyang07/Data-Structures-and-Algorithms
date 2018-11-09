# Insert Delete GetRandom O(1)
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.idx_map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.idx_map:
            return False
        self.values.append(val)
        self.idx_map[val] = len(self.values) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.idx_map:
            return False
        # do not use .pop() in case val is the last element
        # which index then will be added back to idx_map without del self.idx_map[val]
        idx = self.idx_map[val]
        self.values[idx], self.values[-1] = self.values[-1], self.values[idx]
        self.idx_map[self.values[idx]] = idx
        # clean up val and its index
        self.values.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.values[random.randint(0, len(self.values) - 1)]
