# Path Sum II
# DFS + stack
def path_sum(root, target):
    if not root:
        return []

    paths = []
    stack = [(root, [root.val])]
    while stack:
        curr, path = stack.pop()
        if not curr.left and not curr.right and sum(path) == target:
            paths.append(path)
        if curr.right:
            stack.append((curr.right, path + [curr.right.val]))
        if curr.left:
            stack.append((curr.left, path + [curr.left.val]))

    return paths


# Max Path Sum
# on every parent node, for left subtree and right subtree respectively
# find a max path that does not cross from a left child to right child (直上直下)
# => knows max path sum of that node
class Solution(object):
    def maxPathSum(self, root):
        if not root:
            raise ValueError('Expecting root node of a tree, None provided')

        self.max_path_sum = float('-inf')  # int var won't be updated in recursion
        self.dfs(root)
        return self.max_path_sum

    def dfs(self, root):
        if not root: return 0
        # max of non-crossing path, do not include a path if its sum is negative
        left_max = max(self.dfs(root.left), 0)
        right_max = max(self.dfs(root.right), 0)
        # update with max of possibly crossing path
        self.max_path_sum = max(self.max_path_sum, root.val + left_max + right_max)
        # pick either left or right max
        return root.val + max(left_max, right_max)
