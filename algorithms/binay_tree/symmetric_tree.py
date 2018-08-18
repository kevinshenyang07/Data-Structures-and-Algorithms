from collections import deque

# Symmetric Tree
# recursive
def is_symmetric(root):
    if not root: return True
    return is_mirror(root.left, root.right)

def is_mirror(self, p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)

# iterative
def is_symmetric_iter(root):
    if not root: return True
    # process in pairs
    queue = deque([(root.left, root.right)])
    while queue:
        p, q = queue.popleft()

        if not p and not q: continue
        if not p or not q: return False
        if p.val != q.val: return False

        queue.append((p.left, q.right))
        queue.append((p.right, q.left))

    return True
