from __future__ import print_function
import string
from linked_list import LinkedList

# implemented with an array of linked lists
# using built-in hash function
class HashMap(object):
    def __init__(self, capacity=8):
        # each bucket is a linked list
        self.capacity = capacity
        self.count = 0
        self.store = self.create_store(capacity)

    def create_store(self, capacity):
        store = []
        for i in range(capacity):
            store.append(LinkedList())
        return store

    # override `in` operator
    def __contains__(self, key):
        bucket = self.get_bucket(key)
        return bucket.has_key(key)

    def __getitem__(self, key):
        bucket = self.get_bucket(key)
        return bucket[key]

    # set or update
    def __setitem__(self, key, val):
        if self.count == self.capacity:
            self.resize()
        bucket = self.get_bucket(key)
        if bucket.has_key(key):
            bucket.update(key, val)
        else:
            bucket.append(key, val)
            self.count += 1

    def __delitem__(self, key):
        bucket = self.get_bucket(key)
        bucket.remove(key)
        self.count -= 1

    def __iter__(self):
        for bucket in self.store:
            for node in bucket:
                yield node.key

    def __len__(self):
        return self.count

    def __repr__(self):
        if self.count == 0:
            return "{}"
        pairs = "\n".join(["  {}: {},".format(k, self[k]) for k in self])
        return "{\n" + pairs + "\n}"

    def resize(self):
        new_capacity = self.capacity * 2
        new_store = self.create_store(new_capacity)
        for k in self:
            # index in the new_store array
            i = hash(k) % new_capacity
            new_store[i].append(k, self[k])
        self.capacity = new_capacity
        self.store = new_store
        print("Resized!")

    def get_bucket(self, key):
        hashed_key = hash(key) % len(self.store)
        return self.store[hashed_key]


if __name__ == '__main__':
    hash_map = HashMap()
    keys = string.lowercase[:10]
    for i in range(len(keys)):
        hash_map[keys[i]] = i
    print(hash_map)
    print("a" in hash_map)  # True
    del hash_map["a"]
    del hash_map["b"]
    print(hash_map)
    # it should call resize() when enough items are inserted
    # it should rehash existing values
