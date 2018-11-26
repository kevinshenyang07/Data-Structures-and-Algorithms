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

        self.roots = collections.defaultdict(list)  # signature => list of roots
        self.postorder(root)
        return [roots[0] for roots in self.roots.values() if len(roots) > 1]


    # get id of the subtree
    def postorder(self, node):
        if not node: return 0

        left_sig = self.postorder(node.left)
        right_sig = self.postorder(node.right)
        # do not hash the sum of nodes since the values can have duplicates
        rroot_sig = hash("{}/{}\{}".format(left_sig, node.val, right_sig))
        self.roots[root_sig].append(node)
        return root_sig
# O(n) time and space
