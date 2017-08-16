from __future__ import print_function


# doulbly linked list
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return "Node {}: {}".format(self.key, self.val)

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
        self.head = Node("dummay_head", None)
        self.tail = Node("dummay_tail", None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # in this case, does not support negative index
    def __getitem__(self, key):
        for node in self:
            if node.key == key:
                return node.val
        raise IndexError("key not found")

    # override for .. in ..
    def __iter__(self):
        curr = self.head
        while curr.next and curr.next.next:
            yield curr.next
            curr = curr.next

    def __repr__(self):
        return " - ".join(["({}: {})".format(node.key, node.val) for node in self])

    def first(self):
        return self.head.next

    def last(self):
        return self.tail.prev

    def append(self, key, val):
        last = self.tail.prev
        node = Node(key, val)
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

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

    def has_key(self, key):
        for node in self:
            if node.key == key:
                return True
        return False

    def is_empty(self):
        return (self.head.next == self.tail) and (self.tail.prev == self.head)

    # iterative
    def reverse(self):
        # return if linked list is empty or has only one node
        if self.is_empty() or self.first() == self.last():
            return
        temp = None
        curr = self.head
        # swap next and prev for all nodes
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        # swap the refence of head and tail
        self.head, self.tail = self.tail, self.head

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append("first", 1)
    linked_list.append("second", 2)
    linked_list.append("third", 3)
    print(linked_list)
    linked_list.update("first", 4)
    print(linked_list)

    print(linked_list["first"])  # 4
    # print(linked_list.get("fourth"))  # error
    linked_list.remove("first")


    print(linked_list.first().next.key)  # third

    print("iterating through linked list:")
    for node in linked_list:
        print(node)

    print("reversing linked list")
    linked_list.reverse()
    print(linked_list)
    print(linked_list.head)
