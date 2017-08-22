# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def depth(root):
    if not root:
        return 0
    return max(depth(root.left), depth(root.right)) + 1


# the depth of the two subtrees of every node never differ by more than 1
def is_balanced(root):
    if not root:
        return True
    if (not root.left) and (not root.right):
        return True
    if abs(depth(root.left) - depth(root.right)) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


def inorder_rec(root, arr=[]):
    if root:
        inorder_rec(root.left, arr)
        arr.append(root.val)
        inorder_rec(root.right, arr)
    return arr


def inorder(root):
    stack = []
    visited = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            visited.append(root.val)
            root = root.right
    return visited



