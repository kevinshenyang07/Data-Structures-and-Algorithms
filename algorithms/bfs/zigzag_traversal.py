# Binary Tree Zigzag Level Order Traversal
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        level = [root]
        reverse = False
        visited = []
        # each level keeps its original order, but saved to visited depending on the flag
        while level:
            if reverse:
                vals = [level[i].val for i in range(len(level) - 1, -1, -1)]
            else:
                vals = [level[i].val for i in range(len(level))]

            visited.append(vals)
            reverse = not reverse

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return visited
