import collections

# couple of ways
# 1. level order traversal should only have one missing node
# 2. is_complete(root) = is_complete(root.left) and is_full(root.right)
def is_complete(root):
    if not root:
        return True

    queue = collections.deque([root])
    has_missing = False

    while queue:
        node = queue.popleft()

        if has_missing and node:
            return False
        if not node:
            has_missing = True
        else:
            queue.append(node.left)
            queue.append(node.right)

    return True

# followup: given a array of values, construct complete binary tree
def build_tree(vals):
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = collections.deque([(root, 0)])

    while queue:
        node, i = queue.popleft()

        if 2 * i + 1 < len(vals):
            node.left = TreeNode(vals[2 * i + 1])
            queue.append((node.left, 2 * i + 1))
        if 2 * i + 2 < len(vals):
            node.right = TreeNode(vals[2 * i + 2])
            queue.append((node.right, 2 * i + 2))

    return root

def print_tree(root):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        print node.val
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def test1():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node4.left = node6

    print is_complete(node1)

def test2():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node2.left = node4

    print is_complete(node1)


def test3():
    root = build_tree(range(1, 9))
    print_tree(root)

if __name__ == '__main__':
    test1()
    test2()
    test3()
