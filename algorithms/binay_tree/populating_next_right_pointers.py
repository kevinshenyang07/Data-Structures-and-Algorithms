from tree_node import TreeLinkNode


# Populating Next Right Pointers in Each Node II
# use only constant space
# in problem I, assume it's a perfect tree (all leaves are at the same level, and every parent has two children)
# in problem II, no longer assume it's a perfect tree
# Idea: build the next relationship in the next level, then traverse that level by next pointers
class Solution:
    def connect(self, root):
        dummy = TreeLinkNode(0)
        prev = dummy  # node to be connected to the next

        while root:
            if root.left:
                prev.next = root.left
                prev = prev.next
            if root.right:
                prev.next = root.right
                prev = prev.next

            root = root.next
            if not root:  # go to next level
                prev = dummy  # reset prev
                root = dummy.next  # leftmost node in next level
                dummy.next = None
