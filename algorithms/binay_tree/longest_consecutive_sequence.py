# Binary Tree Longest Consecutive Sequence
# Given a binary tree, find the length of the longest consecutive sequence path.
# The path needs to be from parent to child (cannot be the reverse).
# "consecutive" means increasing by 1 each time
class SolutionQ1(object):
    def longest_consecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.preorder(root, root, 0)

    def preorder(self, node, parent, max_length):
        """
        returns longest consecutive path starting from node
        """
        if not node: return max_length

        if node.val == parent.val + 1:
            max_length += 1
        else:
            max_length = 1

        left_length = self.preorder(node.left, node, max_length)
        right_length = self.preorder(node.right, node, max_length)

        return max(max_length, left_length, right_length)


# Binary Tree Longest Consecutive Sequence II
# this time, this path can be either increasing or decreasing,
# and the path can be in the child-Parent-child order
#   2
#  / \
# 1   3
# => 3
class SolutionQ2(object):
    def longest_consecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_length = [0]
        self.postorder(root, root, max_length)
        return max_length[0]

    def postorder(self, node, parent, max_length):
        """
        returns longest increasing / decreasing path length starting from node
        """
        if not node: return 0, 0

        li, ld = self.postorder(node.left, node, max_length)
        ri, rd = self.postorder(node.right, node, max_length)

        max_length[0] = max(max_length[0], li + rd + 1, ld + ri + 1)

        if node.val == parent.val + 1:  # increasing from parent
            return max(li, ri) + 1, 0
        if node.val == parent.val - 1:  # decreasing from parent
            return 0, max(ld, rd) + 1

        return 0, 0
