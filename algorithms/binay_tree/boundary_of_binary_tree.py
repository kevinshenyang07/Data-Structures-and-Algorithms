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
        if not root: return []

        boundary = [root.val]
        self.left_bound(root.left, boundary)
        self.leaves(root.left, boundary)
        self.leaves(root.right, boundary)
        self.right_bound(root.right, boundary)

        return boundary

    # preorder
    def left_bound(self, root, boundary):
        if not root or (not root.left and not root.right):
            return
        boundary.append(root.val)
        if root.left:
            self.left_bound(root.left, boundary)
        else:
            self.left_bound(root.right, boundary)

    # postorder
    def right_bound(self, root, boundary):
        if not root or (not root.left and not root.right):
            return
        if root.right:
            self.right_bound(root.right, boundary)
        else:
            self.right_bound(root.left, boundary)
        boundary.append(root.val)

    # DFS
    # level order does not work for get leaves
    # since it add leaves not at the last level first，
    # which should actually be the last
    def leaves(self, root, boundary):
        if not root:
            return
        if not root.left and not root.right:
            boundary.append(root.val)
            return
        self.leaves(root.left, boundary)
        self.leaves(root.right, boundary)

