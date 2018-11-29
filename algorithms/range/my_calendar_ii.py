# My Calendar II
class MyCalendarTwo(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        if not self.root.insertable(start, end):
            return False
        self.root.insert(start, end)
        return True
# O(logn) ~ O(n) time for each book() call, since in worst case BST will be a list

class TreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.count = 1

    def insertable(self, start, end):
        # non-overlapping
        if self.end <= start:
            if not self.right:
                return True
            return self.right.insertable(start, end)
        elif self.start >= end:
            if not self.left:
                return True
            return self.left.insertable(start, end)
        # overlapping
        else:
            if self.count > 1:
                return False
            if self.end < end and not self.insertable(self.end, end):
                return False
            if self.start > start and not self.insertable(start, self.start):
                return False
            return True

    def insert(self, start, end):
        # non-overlapping
        if self.end <= start:
            if not self.right:
                self.right = TreeNode(start, end)
            else:
                self.right.insert(start, end)
        elif self.start >= end:
            if not self.left:
                self.left = TreeNode(start, end)
            else:
                self.left.insert(start, end)
        # overlapping
        else:
            s_min, s_max = sorted([self.start, start])
            e_min, e_max = sorted([self.end, end])
            # shrink the range of current node, insert extra range(s)
            self.start = s_max
            self.end = e_min
            self.count += 1
            self.insert(s_min, s_max)
            self.insert(e_min, e_max)
