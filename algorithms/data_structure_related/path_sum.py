import sys

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
def max_path_sum(root):
    min_int = - sys.maxint - 1
    if not root: return min_int
    global_max = [min_int]  # int var won't be updated in recursion

    dfs(root, global_max)
    return global_max[0]

def dfs(root, global_max):
    if not root: return 0
    # max of non-crossing path
    left_max = max(dfs(root.left, global_max), 0)
    right_max = max(dfs(root.right), 0)
    # update with max of possibly crossing path
    global_max[0] = max(global_max[0], root.val + left_max + right_max)
    # pick either left or right max
    return root.val + max(left_max, right_max)