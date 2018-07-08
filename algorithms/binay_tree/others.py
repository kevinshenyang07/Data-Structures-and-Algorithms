from tree_node import TreeNode


# divide & conquer version
def depth(root):
    if not root:
        return 0
    return max(depth(root.left), depth(root.right)) + 1

# iterative version, preorder
def depth_iter(root):
    if not root:
        return 0
    stack_node = [root]
    stack_depth = [1]
    max_depth = 0
    while stack_node:
        node = stack_node.pop()
        depth = stack_depth.pop()
        max_depth = max(max_depth, depth)
        if node.right:
            stack_node.append(node.right)
            stack_depth.append(depth + 1)
        if node.left:
            stack_node.append(node.left)
            stack_depth.append(depth + 1)
    return max_depth


# Balanced Binary Tree
# the depth of the two subtrees of every node never differ by more than 1
def is_balanced(root):
    if not root:
        return True
    if (not root.left) and (not root.right):
        return True
    if abs(depth(root.left) - depth(root.right)) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


# Construct Binary Tree from Preorder and Inorder Traversal
def build_tree(preorder, inorder):
    # preorder and inorder are lists of node values
    # return the root of built tree
    # assumption: no duplicates
    if inorder:
        root_val = preorder.pop(0)
        root_idx = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = build_tree(preorder, inorder[:root_idx])
        root.right = build_tree(preorder, inorder[root_idx+1:])
        return root
    else:
        return None


# Path Sum
def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right and root.val == target:
        return True
    target -= root.val
    return has_path_sum(root.left, target) or has_path_sum(root.right, target)


# Populating Next Right Pointers in Each Node
def connect(root):
    while root and root.left:
        next = root.left  # save the next node to be visited
        while root:
            root.left.next = root.right
            # null if no sibling node, otherwise jump to another root
            # and connect to its left child
            root.right.next = root.next and root.next.left
            root = root.next  # move right at the same level
        root = next


# Inorder Successor in BST
# iterative version is hard to think of
def inorder_successor(root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None

    if root.val <= p.val:
        return inorder_successor(root.right, p)
    else:
        left = inorder_successor(root.left, p)
        return left if left else root
# O(logn) time and space


# Verify Preorder Sequence in Binary Search Tree
# f([5,2,6,1,3]) => False; f([5,2,1,3,6]) => True
# assume each number in the sequence is unique.
def verify_preorder(preorder):
    """
    :type preorder: List[int]
    :rtype: bool
    """
    low = - 2 ** 31  # lower bound of next right child's value
    stack = []  # top element being current root
    for val in preorder:
        if val < low:
            return False
        while stack and stack[-1] < val:
            low = stack.pop()  # go up and update lower bound
        stack.append(val)

    return True
