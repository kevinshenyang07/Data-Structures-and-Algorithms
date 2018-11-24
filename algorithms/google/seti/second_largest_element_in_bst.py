# write a function to return the second largest node in a BST
# break it down to cases below:
# 1. not enough nodes
# 2. no right subtree: find the largest in left subtree
# 3. the right child does not have child nodes: returns root
# 4. otherwise: find the 2nd largest in root.right
def second_largest(root):
    if not root or (not root.left and not root.right)
        raise ValueError('must have at least 2 nodes')  # depending on requirement
    if not root.right:
        return largest(root.left)
    if not root.right.left and not root.right.right:
        return root.val
    return second_largest(root.right)

def largest(root):
    while root.right:
        root = root.right
    return root.val
