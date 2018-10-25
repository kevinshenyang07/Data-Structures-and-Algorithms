# Count Univalue Subtrees
# to be the root node of a valid subtree:
# 1. if its val is the same as its left/right child's value
# 2. both left and right subtrees are valid

# approach: bottom up with postorder since it can carry info from children
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cnt = 0
        self.postorder(root)
        return self.cnt

    def postorder(self, node):
        if not node:
            return True

        valid_left = self.postorder(node.left)
        valid_right = self.postorder(node.right)

        univalue = True
        if node.left and node.left.val != node.val:
            univalue = False
        if node.right and node.right.val != node.val:
            univalue = False

        if valid_left and valid_right and univalue:
            self.cnt += 1
            return True
        return False
