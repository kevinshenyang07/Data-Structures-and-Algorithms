# self.key is needed to delete the entry in cache.node_map when eject
class ListNode(object):
    def __init__(self, key, val, expire_at=-1):
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
