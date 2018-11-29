# Find Duplicate Subtrees
# to compare any two subtrees, create a signature for each subtree
# with root.val, signature of left / right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root: return []

        self.sigs = set()
        self.dups = {}  # signature => root of duplicate subtree
        self.postorder(root)
        return self.dups.values()

    def postorder(self, node):
        if not node: return 0

        left_sig = self.postorder(node.left)
        right_sig = self.postorder(node.right)
        # do not hash the sum of nodes since the values can have duplicates
        root_sig = hash("{}/{}\{}".format(left_sig, node.val, right_sig))

        self.roots[root_sig].append(node)
        return root_sig
# O(n) time and space
