import time
from linked_list import LinkedList, ListNode

# Map With Expiration (from Google)
# Design a hashmap with expiration time, it should support the following operations:
# get(key): Get the value, delete the entry if expired
# put(key, value, expire): Expire in `expire` seconds.
# prune(): Remove all expired entries.
class ExpiringMap(object):

    def __init__(self):
        self.node_map = {}
        self.list = LinkedList()
        # import threading
        # self.lock = threading.RLock()

    def get(self, key):
        # try:
        #     self.lock.acquire()
        self.prune()

        if key not int self.node_map:
            return None
        if self.node_map[key].expire_at <= time.time():
            self.list.remove(self.node_map[key])
            self.node_map.pop(key)
            return None
        return self.node_map[key].val
        # finally:
        #     self.lock.release()

    def put(self, key, value, expire):
        # try:
        #     self.lock.acquire()
        expired_at = time.time() + expire

        if key not in self.node_map:
            node = ListNode(key, val, time.time() + expire)
            self.node_map[key] = node
            self.list.append(node)
        else:
            node = self.node_map[key]
            node.val = value
            node.expired_at = expired_at
        # finally:
        #     self.lock.release()

    def prune(self):
        while not self.list.is_empty():
            first = self.list.head.next
            if first.expire_at <= time.time():
                self.node_map.pop(first.key)
                self.list.popleft()
            else:
                break
