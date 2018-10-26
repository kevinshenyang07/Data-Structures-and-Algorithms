# design a map with key to be double
# if calling get() with key within range of original key +- epsilon,
# return its original value
class EpsilonMap(object):
    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.key_map = {}
        self.val_map = {}  # bucket index => val

    def bucket(self, key):
        return int(key / self.epsilon)

    # assume keys does not have overlapping ranges
    def put(self, key, val):
        k = self.bucket(key)
        self.key_map[k] = key
        self.val_map[k] = val

    # assume getting map[k - 1] first
    def get(self, key):
        k = self.bucket(key)
        if k in self.val_map:
            return self.val_map[k]
        if k - 1 in self.val_map:
            return self.val_map[k - 1]
        if k + 1 in self.val_map:
            return self.val_map[k + 1]
        return None
