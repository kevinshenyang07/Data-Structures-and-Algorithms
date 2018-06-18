# Count Univalue Subtrees
# to be the root node of a valid subtree:
# 1. if its val is the same as its left/right child's value
# 2. both left and right subtrees are valid

# approach: bottom up with postorder since it can carry info from children
class Solution(object):
    def count_unival_subtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.postorder(root, res)
        return res[0]

    def postorder(self, node, res):
        if not node:
            return True

        valid_left = self.postorder(node.left, res)
        valid_right = self.postorder(node.right, res)

        univalue = True
        if node.left and node.left.val != node.val:
            univalue = False
        if node.right and node.right.val != node.val:
            univalue = False

        if valid_left and valid_right and univalue:
            res[0] += 1
            return True
        return False
