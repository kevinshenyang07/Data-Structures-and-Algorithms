# Binary Tree Longest Consecutive Sequence
# Given a binary tree, find the length of the longest consecutive sequence path.
# The path needs to be from parent to child (cannot be the reverse).
# "consecutive" means increasing by 1 each time
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.max_len = 1
        self.preorder(root, 1)
        return self.max_len

    def preorder(self, root, length):
        self.max_len = max(self.max_len, length)

        if root.left:
            if root.val + 1 == root.left.val:
                self.preorder(root.left, length + 1)
            else:
                self.preorder(root.left, 1)

        if root.right:
            if root.val + 1 == root.right.val:
                self.preorder(root.right, length + 1)
            else:
                self.preorder(root.right, 1)


# Binary Tree Longest Consecutive Sequence II
# this time, this path can be either increasing or decreasing,
# and the path can be in the child-Parent-child order
#   2
#  / \
# 1   3
# => 3
class Solution(object):
    def longest_consecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_length = 0
        self.postorder(root, root)
        return self.max_length

    def postorder(self, node, parent):
        """
        returns longest increasing / decreasing path length starting from node
        """
        if not node: return 0, 0

        li, ld = self.postorder(node.left, node)
        ri, rd = self.postorder(node.right, node)

        self.max_length = max(self.max_length, li + rd + 1, ld + ri + 1)

        if node.val == parent.val + 1:  # increasing from parent
            return max(li, ri) + 1, 0
        if node.val == parent.val - 1:  # decreasing from parent
            return 0, max(ld, rd) + 1

        return 0, 0
