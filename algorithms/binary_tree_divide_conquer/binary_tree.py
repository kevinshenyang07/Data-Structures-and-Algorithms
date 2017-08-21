# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def inorder_rec(root, arr=[]):
    if root:
        inorder_rec(root.left, arr)
        arr.append(root.val)
        inorder_rec(root.right, arr)
    return arr

# the depth of the two subtrees of every node never differ by more than 1


def depth(root):
    if not root:
        return 0
    

def is_balanced(root):
