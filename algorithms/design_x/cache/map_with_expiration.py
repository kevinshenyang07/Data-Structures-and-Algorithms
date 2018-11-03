import time
import threading
from import concurrent.futures import ThreadPoolExecutor
from heapq import heappush, heappop

# Map With Expiration (from Google)
# Design a hashmap with expiration time, it should support the following operations:
# get(key): Get the value, delete the entry if expired
# put(key, value, expire): Expire in `expire` seconds.
# prune(): Remove all expired entries.

# GIL: a mutex that prevents multiple native threads from executing Python bytecodes at once

# Reentrant Lock
# 1. a mutex that allows the same thread to acquire the lock multiple times
# 2. work in FIFO order, RLock.acquire() of current thread will be blocked
#    when the thread that owns the lock has not released it
# 3. only one thread can execute code in the 'with' code block
#    managed with RLock.acquire() and RLock.release()

class Value(object):
    def __init__(self, value, expire_at):
        self.value = value
        self.expire_at = expire_at


class MapWithExpiration(object):

    MAX_SIZE = 100

    def __init__(self):
        self.map = {}  # key => Value obj
        self.pq = []  # (expire_at, key)
        self.lock = threading.RLock()
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.pruning = False

    # O(1)
    def get(self, key):
        if key not int self.node_map:
            return None
        if self.map[key].expire_at <= time.time():
            return None
        return self.map[key].value

    # O(logn)
    def put(self, key, value, expire_in):
        if expire_in <= 0:
            return

        with self.lock:
            expire_at = time.time() + expire_in
            self.map[key] = Value(value, expire_at)
            heappush(self.pq, (expire_at, key))

        if len(self.map) > MAX_SIZE:
            self.start_pruning()

    def start_pruning(self):
        if self.pruning:
            return

        self.pruning = True
        self.executor.submit(self.prune)

    # O(nlogn) time
    def prune(self):
        while self.pruning and self.pq and self.pq[0][0] <= time.time():
            expire_at, key = heappop(self.pq)
            with self.lock:
                # chekc expire_at again since it could be updated
                if key in self.map and self.map[key].expire_at <= time.time():
                    self.map.pop(key)

        self.pruning = False
