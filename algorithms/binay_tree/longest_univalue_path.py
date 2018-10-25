# Longest Univalue Path
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.longest = 0
        self.postorder(root, root.val)
        return self.longest

    # longest path with node.val from node to left / right
    # utilize both left + right and max(left, right)
    def postorder(self, node, target):
        if not node:
            return 0

        left = self.postorder(node.left, node.val)
        right = self.postorder(node.right, node.val)

        self.longest = max(self.longest, left + right)

        if node.val == target:
            return max(left, right) + 1
        else:
            return 0
# O(n) time and space
