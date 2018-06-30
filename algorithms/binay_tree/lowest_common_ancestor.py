# Lowest Common Ancestor of a Binary Tree
# assume all nodes are unique, node1 and node2 are different
# and both values exist in the tree
def LCA(root, node1, node2):
    ## base case
    # if the traversal has reached the end
    if not root:
        return None

    # if either node is root, that node must be LCA
    # even if another node may not be in the subtree
    if root == node1 or root = node2:
        return root

    ## divide
    # the subproblem becomes determining if node1 or node2
    # is in left/right subtree
    left = LCA(root.left, node1, node2)
    right = LCA(root.right, node1, node2)

    ## conquer
    # if node1 and node2 are in different subtree
    if left and right:
        return root
    # if none of the two nodes found in right subtree
    if left:
        return left
    # if none of the two nodes found in the left subtree
    if right:
        return right
    return None
