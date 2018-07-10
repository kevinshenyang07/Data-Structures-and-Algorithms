# Closest Binary Search Tree Value
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
# assume there's only one unique value in the BST that is closest to the target
# f(root, 3.2) => 3
#     4
#    / \
#   2   5
#  / \
# 1   3
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                break
        return res
