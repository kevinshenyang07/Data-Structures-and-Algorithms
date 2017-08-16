from __future__ import print_function


# doulbly linked list
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return "{}: {}".format(self.key, self.val)

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
        return self


class LinkedList(object):
    def __init__(self):
        # create two dummy nodes for start and end
        self.start = Node("dummay_start", None)
        self.end = Node("dummay_end", None)
        self.start.next = self.end
        self.end.prev = self.start

    # in this case, does not support negative index
    def __getitem__(self, idx):
        curr = self.start.next
        for i in range(idx):
            if curr.next:
                curr = curr.next
            else:
                raise IndexError('index out of range')
        return curr

    # override for .. in ..
    def __iter__(self):
        curr = self.start
        while curr.next and curr.next.next:
            yield curr.next
            curr = curr.next

    def __repr__(self):
        return " <-> ".join(["{}: {}".format(node.key, node.val) for node in self])

    def first(self):
        return self.start.next

    def last(self):
        return self.end.prev

    def get(self, key):
        for node in self:
            if node.key == key:
                return node.val
        raise IndexError("key not found")

    def append(self, key, val):
        last = self.end.prev
        node = Node(key, val)
        last.next = node
        node.prev = last
        node.next = self.end
        self.end.prev = node

    def update(self, key, val):
        for node in self:
            if node.key == key:
                node.val = val
                return node
        raise IndexError("key not found")

    def remove(self, key):
        for node in self:
            if node.key == key:
                node.remove()
                return node
        raise IndexError("key not found")


linked_list = LinkedList()
linked_list.append("first", 1)
linked_list.append("second", 2)
linked_list.append("third", 3)
print(linked_list)
linked_list.update("first", 4)
print(linked_list)

print(linked_list.get("first"))  # 4
# print(linked_list.get("fourth"))  # error
linked_list.remove("first")


print(linked_list.first().next.key)  # third

print("iterating through linked list:")
for node in linked_list:
    print(node)

print(linked_list[1])
