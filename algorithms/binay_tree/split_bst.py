# Split BST
# Given a Binary Search Tree (BST) with root node root, and a target value V,
# split the tree into two subtrees where one subtree has nodes that are all smaller or equal to
# the target value, while the other subtree has all nodes that are greater than the target value.
# It's not necessarily the case that the tree contains a node with value V.
# Additionally, most of the structure of the original tree should remain.
# Assume the BST is valid and each node's value is different.
# Exmaple:
#       4
#     /   \
#   2      6
#  / \    / \
# 1   3  5   7
# => [[2,1],[4,3,6,null,null,5,7]]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]

        # smaller: a tree that all node values <= V
        if root.val < V:
            # node to split is in the right subtree
            smaller, greater = self.splitBST(root.right, V)
            root.right = smaller  # subtree with node values <= V
            return [root, greater]
        elif root.val > V:
            # node to split is in the left subtree
            smaller, greater = self.splitBST(root.left, V)
            root.left = greater  # subtree with node value > V
            return [smaller, root]
        else:
            right = root.right  # subtree with node values > V
            root.right = None
            return [root, right]
