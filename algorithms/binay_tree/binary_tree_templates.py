from collections import deque

# preorder: root - left subtree - right subtree (root is pre-children)
# inorder: left subtree - root - right subtree (root is in-children)

def preorder(root):
    if not root:
        return []
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited


def inorder(root):
    stack = []
    visited = []
    while root or stack:
        # to the most left node
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        visited.append(root.val)
        root = root.right
    return visited


def postorder(root):
    if not root:
        return []
    stack = [root]
    visited = []
    prev, curr = None, root
    while stack:
        curr = stack[-1]
        if not prev or prev.left == curr or prev.right == curr:
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
        elif prev == curr.left:
            if curr.right:
                satck.append(curr.right)
        else:
            visited.append(curr.val)
            stack.pop()
        prev = curr
    return visited


# Validate BST, 理解并背诵
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
        # compare consecutive inorder nodes
        if prev and prev.val >= curr.val:
            return False
        prev = curr
        curr = curr.right  # go up if current node is not a root node
    return True


def level_order(root):
    if not root:
        return []
    queue = deque([root])
    visited = []
    while queue:
        level = []
        size = len(queue)  # queue size changes within the loop
        for i in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        visited += level
    return visited
# O(n) in time and space
