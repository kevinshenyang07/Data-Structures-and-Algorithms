from collections import deque

# Closest Binary Search Tree Value
# Given a non-empty binary search tree and a target value,
# find the value in the BST that is closest to the target.
# f(root, 3.2) => 3
#     4
#    / \
#   2   5
#  / \
# 1   3
# assume there's only one unique value in the BST that is closest to the target
class Solution(object):
    def closest_value(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val

            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            else:
                break
        return res


# Closest Binary Search Tree Value II
# find k values closest to the target instead of one
# assume k is valid and there's only one unique set of k values in the BST that are closest to the target
# f(root, 3.2, 2) => { 3, 4 }
# order of result doesn't matter
class Solution(object):
    def closest_k_values(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # inorder traversal of BST => sorted values
        queue = deque()
        self.inorder(root, target, k, queue)
        return queue

    def inorder(self, root, target, k, queue):
        if not root or k == 0: return
        if len(queue) == k and queue[0] >= target: return  # diff is only going to be bigger

        self.inorder(root.left, target, k, queue)

        if len(queue) < k:
            queue.append(root.val)
        # queue[0] < target implied here
        # if largest diff in queue is larger than curr diff
        elif (target - queue[0]) > abs(root.val - target):
            queue.popleft()
            queue.append(root.val)

        self.inorder(root.right, target, k, queue)
# O(n) time, O(h) extra space
