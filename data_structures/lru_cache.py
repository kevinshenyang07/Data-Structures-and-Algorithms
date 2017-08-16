from __future__ import print_function
from .hash_map import HashMap
from .linked_list import LinkedList


class LRUCache(object):
    def __init__(self, max, prc):
        self.map = HashMap()
        self.store = LinkedList()
        self.max = max
        self.prc = prc

    def __len__(self):

    def __repr__(self):
        return "Map: {}\nStore: {}".format(self.map, self.store)

    def get(self, key):


    # insert an un-cached key
    def calc(self, key):

    # move a node to the end fo the list
    def update_node(self, node):

    def eject(self):
