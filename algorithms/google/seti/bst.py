# give a node in BST, find the next in-order node
# regular: inorder traversal
# improvement: add .parent attribute to node
def next_node(self, node):
    if not node:
        raise ValueError('not a node')
    if not node.right:
        return node.parent
    # find the smallest in node.left
    node = node.right
    while node.left:
        node = node.left
    return node

# given root of a BST with all nodes' value to be None
# fill it with nums
def fill_bst(self, root, nums):
    stack = []
    i = 0

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if i >= len(nums):
            raise ValueError('not enough numbers to fill BST')

        root.val = nums[i]
        i += 1

        curr = curr.right

# inorder traversal with parent pointer
def inorder(root):
    prev, curr = None, root
    while curr:
        if prev == curr.parent:
            if curr.left:
                prev, curr = curr, curr.left
            else:
                prev = None
        if prev == curr.left:
            print curr.val
            if curr.right:
                prev, curr = curr, curr.right
            else:
                prev = None
        if prev == curr.right:
            prev, curr = curr, curr.parent


class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return self.stack

    def next(self):
        node = self.stack.pop()
        curr = node.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return node.val
