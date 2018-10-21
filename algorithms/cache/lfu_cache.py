from linked_list import LinkedList, ListNode

# LFU Cache
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations:
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
#                   When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
#                   For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
#                   the least recently used key would be evicted.
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_map = {}  # key => node
        self.counter = {}  # key => count
        self.cnt_map = collections.defaultdict(LinkedList)  # count => list
        self.min = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map: return -1

        node = self.node_map[key]
        cnt = self.counter[key]
        self.cnt_map[cnt].remove(node)
        self.cnt_map[cnt + 1].append(node)
        # handle count and min
        self.counter[key] += 1
        if self.min == cnt and self.cnt_map[cnt].is_empty():
            self.min += 1
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.node_map:
            self.get(key)
            self.node_map[key].val = value
            return
        if self.capacity == 0:
            return
        if len(self.node_map) == self.capacity:
            evicted = self.evict_least_freq()
            del self.node_map[evicted.key]
        node = ListNode(key, value)
        self.node_map[key] = node
        self.cnt_map[1].append(node)
        self.counter[key] = 1
        self.min = 1

    def evict_least_freq(self):
        """
        :rtype: ListNode
        """
        curr_list = self.cnt_map[self.min]
        node = curr_list.popleft()
        if curr_list.is_empty():
            self.min += 1
        return node
