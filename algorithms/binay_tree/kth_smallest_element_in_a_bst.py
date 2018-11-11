# Kth Smallest Element in a BST
# assume 1 <= k <= tree size
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

# What if the BST is modified (insert / delete operations) often and you need to find
# the kth smallest frequently? How would you optimize the kthSmallest routine?
# Approach: each node keep track of the size of its left subtree
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left_cnt = 0
        self.left = None
        self.right = None

    def insert(self, val):
        pass

    def delete(self, val):
        pass

class Solution(object):
    def kthSmallest(self, root, k):
        if root.left_cnt + 1 < k:
            return self.kthSmallest(self, root.right, k - root.left_cnt - 1)
        elif root.left_cnt + 1 > k:
            return self.kthSmallest(self, root.left, k)
        else:
            return root.val
