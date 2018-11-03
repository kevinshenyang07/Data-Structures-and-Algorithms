from linked_list import ListNode

# LRU Cache
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations:
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
#                   When the cache reached its capacity, it should invalidate
#                   the least recently used item before inserting a new item.
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_map = {}  # key => node
        self.list = LinkedList() # latest at tail

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map: return -1

        node = self.node_map[key]
        self.list.remove(node)
        self.list.append(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.list.remove(node)
            self.list.append(node)
            return
        if len(self.node_map) == self.capacity:
            # eject the least recent node and remove from mapping
            first = self.list.popleft()
            self.node_map.pop(first.key)
        node = ListNode(key, value)
        self.list.append(node)
        self.node_map[key] = node


