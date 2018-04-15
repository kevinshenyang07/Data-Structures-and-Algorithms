from __future__ import print_function
import math
from hash_map import HashMap
from linked_list import Node, LinkedList

# a linked list to store k-v pair, append the most recent item at the end
# a hash map to store k-ref pair for O(1) lookup
class LRUCache(object):
    def __init__(self, capacity):
        self.map = HashMap()
        self.list = LinkedList()
        self.capacity = capacity

    def get(self, key):
        # assume values are positive
        if key not in self.map:
            return -1
        node = self.map[key]
        self.list.remove(node)
        self.list.append(node)
        return node.val

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.list.remove(node)
            self.list.append(node)
            return
        if len(self.map) == self.capacity:
            node_first = self.list.remove(self.list.first())
            del self.map[node_first.key]
        node = Node(key, value)
        self.list.append(node)
        self.map[key] = node

    # remvove least recent node
    def eject(self):
        node = self.list.first()
        self.list.remove(node)
        del self.map[node.key]


if __name__ == '__main__':
   cache = LRUCache(capacity=8)
   for i in range(10):
       cache.put(i, i)
   print(cache)
   print(cache.get(5))  # 25
   print(cache)
