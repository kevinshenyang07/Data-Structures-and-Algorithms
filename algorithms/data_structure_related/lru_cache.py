
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
