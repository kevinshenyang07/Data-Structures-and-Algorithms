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


# the depth of the two subtrees of every node never differ by more than 1
def is_balanced(root):
    if not root:
        return True
    if (not root.left) and (not root.right):
        return True
    if abs(depth(root.left) - depth(root.right)) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


def inorder_rec(root, arr=[]):
    if root:
        inorder_rec(root.left, arr)
        arr.append(root.val)
        inorder_rec(root.right, arr)
    return arr


def inorder(root):
    stack = []
    visited = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        visited.append(root.val)
        root = root.right
    return visited


def is_valid_bst(root):
    if not root:
        return True
    stack = []
    prev, curr = None, root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if prev and prev.val > curr.val:
            return False
        prev = curr
        curr = curr.right
    return True


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


def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right and root.val == target:
        return True
    target -= root.val
    return has_path_sum(root.left, target) or has_path_sum(root.right, target)


def LCA(root, node1, node2):
    # base cases
    if root is None or root == node1 or root == node2:
        return root
    # divide
    left = LCA(root.left, node1, node2)
    right = LCA(root.right, node1, node2)
    # conquer
    # if node1 and node2 are in different subtrees
    if left and right:
        return root
    if left:
        return left
    if right:
        return right
    return None


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
