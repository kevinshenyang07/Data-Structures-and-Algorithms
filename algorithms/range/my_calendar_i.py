# My Calendar I
class Node:
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.left = None
        self.right = None


class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True

        return self.insert(self.root, start, end)

    def insert(self, node, s, e):
        # if falling into the first two conditions, [s, e)
        # must not have any overlap with current node (and its parent nodes)
        # thus we only need to compare with current node
        if e <= node.start:
            if node.left:
                return self.insert(node.left, s, e)
            else:
                node.left = Node(s, e)
                return True
        elif node.end <= s:  # always use < to make it more intuitive
            if node.right:
                return self.insert(node.right, s, e)
            else:
                node.right = Node(s, e)
                return True
        else:
            return False
# O(logn) ~ O(n) time for each book() call, since in worst case BST will be a list
