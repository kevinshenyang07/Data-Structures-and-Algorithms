# Unique Binary Search Trees II
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0: return []
        return self.generateChildren(1, n)

    def generateChildren(self, i, j):
        if i > j: return [None]
        if i == j: return [TreeNode(i)]

        children = []
        # Divide & Conquer
        for k in range(i, j + 1):
            children_left = self.generateChildren(i, k - 1)
            children_right = self.generateChildren(k + 1, j)

            for cl in children_left:
                for cr in children_right:
                    root = TreeNode(k)
                    root.left = cl
                    root.right = cr
                    children.append(root)

        return children
