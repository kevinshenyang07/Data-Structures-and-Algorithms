# Recover Binary Search Tree
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))  # dummy node
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, root):
        if root == None: return

        self.traverse(root.left)

        # passing prev as arg will lose track of it in the traverse above
        if not self.first and self.prev.val >= root.val:
            self.first = self.prev
        if self.first and self.prev.val >= root.val:
            self.second = root
        self.prev = root

        self.traverse(root.right)
# thought process
# naive approcah: traverse in order and find the irregular pair
# improvement: only keep track of prev node and curr node
# eg the traversal result of
#    1
#   /
#  3
#   \
#    2
# would be [3, 2, 1] => find the first and last pair that pair[0] > pair[1]
#                    => swap pair1[0] with pair2[1]
