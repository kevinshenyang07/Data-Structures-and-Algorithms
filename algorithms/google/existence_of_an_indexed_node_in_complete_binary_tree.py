# give a complete binary tree with root indexed as 0, root.left indexed as 1 and so on
# find if a node with index i exists
def has_index(root, i):
    if not root or i < 0:
        return False
    if i == 0:
        return True

    path = []  # bools to determine if current root should go left or right

    while i > 0:
        path.append(i % 2 == 1)
        i = (i - 1) / 2

    while root and path:
        go_left = path.pop()
        if go_left:
            root = root.left
        else:
            root = root.right

    return bool(root)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def test(N):
    nodes = []

    for i in range(N):
        nodes.append(Node(i))

    for i in range(N):
        if i * 2 + 1 < N:
            nodes[i].left = nodes[i * 2 + 1]
        if i * 2 + 2 < N:
            nodes[i].right = nodes[i * 2 + 2]

    print has_index(nodes[0], -1)
    print has_index(nodes[0], 0)
    print has_index(nodes[0], 7)
    print has_index(nodes[0], 11)
    print has_index(nodes[0], 12)

if __name__ == '__main__':
    test(12)
