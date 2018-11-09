# Boundary of Binary Tree
# Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.
# Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
#     ____1_____
#    /          \
#   2            3
#  / \          /
# 4   5        6
#    / \      / \
#   7   8    9  10
# => [1,2,4,7,8,9,10,6,3]
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # start from root.left/.right to avoid duplicates
        self.boundary = [root.val]
        self.left_bound(root.left)
        self.leaves(root.left)
        self.leaves(root.right)
        self.right_bound(root.right)

        return self.boundary

    # preorder
    def left_bound(self, root):
        if not root or (not root.left and not root.right):
            return
        self.boundary.append(root.val)
        if root.left:
            self.left_bound(root.left)
        else:
            self.left_bound(root.right)

    # postorder
    def right_bound(self, root):
        if not root or (not root.left and not root.right):
            return
        if root.right:
            self.right_bound(root.right)
        else:
            self.right_bound(root.left)
        self.boundary.append(root.val)

    # DFS (level order does not work for get leaves)
    def leaves(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.boundary.append(root.val)
            return
        self.leaves(root.left)
        self.leaves(root.right)
