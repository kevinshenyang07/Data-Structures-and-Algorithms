from __future__ import print_function
import math
from hash_map import HashMap
from linked_list import LinkedList

# a linked list to store k-v pair, append the most recent item at the end
# a hash map to store k-ref pair for O(1) lookup
# the value of each node is func(key)
class LRUCache(object):
    def __init__(self, capacity, func):
        self.map = HashMap()
        self.store = LinkedList()
        self.capacity = capacity
        self.func = func

    def __getitem__(self, key):
        node = self.map[key]
        self.update_node(node)
        return node

    def __len__(self):
        return len(self.map)

    def __repr__(self):
        return "Map: {}\nStore:\n{}".format(self.map, self.store)

    # insert an un-cached key
    def append(self, key):
        if len(self.map) == self.capacity:
            self.eject()
        val = self.func(key)
        self.store.append(key, val)
        self.map[key] = self.store.last()

    # move a node to the end fo the list
    def update_node(self, node):
        node = self.store.remove(node.key)
        self.store.append(node.key, node.val)

    # remvove least recent node
    def eject(self):
        node = self.store.first()
        del self.map[node.key]
        self.store.remove(node.key)


if __name__ == '__main__':
   cache = LRUCache(capacity=8, func=lambda x: pow(x, 2))
   for i in range(10):
       cache.append(i)
   print(cache)
   print(cache[5])  # 25
   print(cache)
