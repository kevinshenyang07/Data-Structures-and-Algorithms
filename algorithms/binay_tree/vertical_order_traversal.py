from collections import deque

# Binary Tree Vertical Order Traversal
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# => [[4], [9,5], [3,0,1], [8,2], [7]]
# If two nodes are in the same row and column, the order should be from left to right.
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        columns = {}
        queue = deque([(root, 0)])

        while queue:
            root, col = queue.popleft()

            columns[col] = columns.get(col, [])
            columns[col].append(root.val)
            # a node is always one column away from its left / right child
            if root.left:
                queue.append((root.left, col - 1))
            if root.right:
                queue.append((root.right, col + 1))

        res = []
        for col in sorted(columns.keys()):
            res.append(columns[col])
        return res
