class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_size = 1  # including itself

# there will be new data coming in, and k could change
# k starts from 1
# iterative version is error-prone
class KthFinder(object):
    def __init__(self):
        self.root = None

    def add(self, val):
        self.root = self.add_helper(self.root, val)

    def add_helper(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.add_helper(root.right, val)
        else:
            root.left_size += 1
            root.left = self.add_helper(root.left, val)
        return root

    # assume k in range [1, n]
    def find(self, k):
        return self.find_helper(self.root, k)

    def find_helper(self, root, k):
        if root.left_size == k:
            return root.val
        if root.left_size < k:
            return self.find_helper(root.right, k - root.left_size)
        else:
            return self.find_helper(root.left, k)

    def level_order(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def test():
    finder = KthFinder()
    vals = [10, 2, 6, 5, 8, 14, 12]
    for val in vals:
        finder.add(val)
    # finder.level_order()

    print finder.find(2)  # 5
    print finder.find(3)  # 6
    print finder.find(6)  # 12

    finder.add(1)
    print finder.find(2)  # 2
    print finder.find(3)  # 5
    print finder.find(6)  # 10


if __name__ == '__main__':
    test()
