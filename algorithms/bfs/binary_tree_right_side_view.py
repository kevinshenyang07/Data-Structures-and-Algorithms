# Binary Tree Right Side View
class BfsSolution(object):
    def right_side_view(self, root):
        # level order
        if not root:
            return []

        res = []
        queue = collections.deque([root])

        while queue:
            count = len(queue)
            while count:
                node = queue.popleft()
                count -= 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)

        return res
# O(n) time and space


class DfsSolution(object):
    def right_side_view(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(res, root, 0)
        return res

    def dfs(self, res, node, level):
        # stop condition
        if not node:
            return
        # valid result condition
        if level == len(res):
            res.append(node.val)
        # recursion
        self.dfs(res, node.right, level + 1)
        self.dfs(res, node.left, level + 1)
# O(n) time and space
