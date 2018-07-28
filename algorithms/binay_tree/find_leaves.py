# Find Leaves of Binary Tree
# Given a binary tree, collect a tree's nodes as if you were doing this:
# collect and remove all leaves, repeat until the tree is empty
# Example:
#     1
#    / \
#   2   3
#  / \
# 4   5
# => [[4, 5, 3], [2], [1]]
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        leaves = []
        self.depth(root, leaves)
        return leaves

    def depth(self, root, leaves):
        if not root: return 0
        # recurse in post order
        left_depth = self.depth(root.left, leaves)
        right_depth = self.depth(root.right, leaves)
        curr_depth = max(left_depth, right_depth) + 1

        if curr_depth > len(leaves):
            leaves.append([])
        # depth is corresponding to the index of sub result
        leaves[curr_depth-1].append(root.val)
        return curr_depth
