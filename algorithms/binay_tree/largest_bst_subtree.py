# Largest BST Subtree
# Given a binary tree, find the BST subtree with largest number of nodes.
# A subtree must include all of its descendants.
#     10
#    /  \
#   5   15
#  / \    \
# 1   8    7
# => 3
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_size = [0]
        self.postorder(root, max_size)
        return max_size[0]

    def postorder(self, root, max_size):
        if not root:
            # to qualify a node without left / right child
            return 2 ** 31 - 1, - 2 ** 31, 0

        left_min, left_max, left_cnt = self.postorder(root.left, max_size)
        right_min, right_max, right_cnt = self.postorder(root.right, max_size)

        # if left / right / current subtree is invalid
        # in this question there're no duplicates
        if left_cnt == -1 or right_cnt == -1 or root.val <= left_max or root.val >= right_min:
            return 0, 0, -1  # min/max doesn't matter

        curr_size = left_cnt + right_cnt + 1
        max_size[0] = max(max_size[0], curr_size)

        return min(left_min, root.val), max(right_max, root.val), curr_size
# O(n) time, O(h) space
