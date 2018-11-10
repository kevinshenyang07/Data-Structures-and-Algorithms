from linked_list import LinkedList, ListNode

# LFU Cache
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations:
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
#                   When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
#                   For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
#                   the least recently used key would be evicted.
# Frequency incremented on both get() and put()
# Approach:
# 1.
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_map = {}  # key => node
        self.list_map = collections.defaultdict(LinkedList)  # count => list with latest node at the end
        self.counter = {}  # key => count
        self.min_cnt = 0  # smallest frequency

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.update(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.update(node)
            return
        # evict first
        if len(self.node_map) == self.capacity:
            self.evict_least_freq()
        # then insert
        node = ListNode(key, value)
        self.node_map[key] = node
        self.list_map[1].append(node)
        self.counter[key] = 1
        self.min_cnt = 1

    # update frequency and related mappings
    def update(self, node):
        """
        :type node: ListNode
        :rtype: void
        """
        cnt = self.counter[node.key]
        self.list_map[cnt].remove(node)
        self.list_map[cnt + 1].append(node)
        self.counter[node.key] += 1
        if self.min_cnt == cnt and self.list_map[cnt].is_empty():
            self.min_cnt += 1

    def evict_least_freq(self):
        """
        :rtype: void
        """
        curr_list = self.list_map[self.min_cnt]
        node = curr_list.popleft()
        self.node_map.pop(node.key)
