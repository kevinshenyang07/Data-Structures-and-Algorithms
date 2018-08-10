from lib import split

# Convert Sorted List to Binary Search Tree
# the BST need to be height-balanced
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        head_left, head_right = split(head)
        root = TreeNode(head_right.val)
        root.left = self.sortedListToBST(head_left)
        root.right = self.sortedListToBST(head_right.next)

        return root

