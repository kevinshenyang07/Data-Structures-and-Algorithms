# My Calendar II
class Node(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.left = None
        self.right = None
        self.overlapped = False

class MyCalendarTwo(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.insertable(self.root, start, end):
            return False

        self.root = self.insert(self.root, start, end)
        return True

    def insertable(self, node, s, e):
        if not node:
            return True
        # no overlap
        if node.start >= e:
            return self.insertable(node.left, s, e)
        if node.end <= s:
            return self.insertable(node.right, s, e)
        # already double-booked
        if node.overlapped:
            return False
        # test range(s) out of [node.start, node.end)
        if s < node.start and not self.insertable(node.left, s, node.start):
            return False
        if node.end < e and not self.insertable(node.right, node.end, e):
            return False
        return True

    def insert(self, node, s, e):
        # base case
        if not node:
            return Node(s, e)
        # no overlap
        if node.start >= e:
            node.left = self.insert(node.left, s, e)
        elif node.end <= s:
            node.right = self.insert(node.right, s, e)
        # otherwise update current node's range
        else:
            s1 = min(node.start, s)
            s2 = max(node.start, s)
            e1 = min(node.end, e)
            e2 = max(node.end, e)

            node.overlapped = True
            node.start = s2
            node.end = e1
            # insert range(s) out of [s2, e1)
            if s1 < node.start:
                node.left = self.insert(node.left, s1, node.start)
            if node.end < e2:
                node.right = self.insert(node.right, node.end, e2)

        return node
# O(logn) ~ O(n) time for each book() call, since in worst case BST will be a list
