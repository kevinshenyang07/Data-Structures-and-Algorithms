from collections import deque

# Binary Tree Zigzag Level Order Traversal
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        levels = []
        queue = deque([root])
        reverse = False

        while queue:
            level = []
            # traverse by level as usual
            for _ in range(len(queue)):
                node = queue.popleft()
                # add visited node differently
                if reverse:
                    level.insert(0, node.val)
                else:
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level)
            reverse = False if reverse else True

        return levels
