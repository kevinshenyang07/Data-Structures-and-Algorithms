# Flatten Binary Tree to Linked List
# Given a binary tree, flatten it to a linked list in-place.
# For example, given the following tree:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = None  # previous node in traversal
        self.postorder(root)

    def postorder(self, root):
        if not root:
            return

        self.postorder(root.right)
        self.postorder(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
