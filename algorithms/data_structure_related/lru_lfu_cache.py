from collections import defaultdict

class ListNode(object):
    def __init__(self, key, val):
        # !! need key to delete the entry in self.nod_map when eject
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = ListNode("Dummy Head", 0)
        self.tail = ListNode("Dummy Tail", 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def popleft(self):
        first = self.head.next
        self.remove(first)
        return first

    def is_empty(self):
        return self.head.next == self.tail


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
            del self.node_map[first.key]
        node = ListNode(key, value)
        self.list.append(node)
        self.node_map[key] = node


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_map = {}  # key => node
        self.counter = {}  # key => count
        self.cnt_map = defaultdict(LinkedList)  # count => list
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
