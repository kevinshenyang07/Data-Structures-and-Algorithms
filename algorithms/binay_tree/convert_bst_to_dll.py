# Convert BST to Doubly Linked List
# the left and right pointers in nodes are to be used as prev and next pointers
# respectively in converted DLL, do it in place
def bst_to_dll(root):
    return inorder(root)[0]

def inorder(root):
    if not root:
        return (None, None)

    head = tail = root

    left_head, left_tail = inorder(root.left)

    if left_head:
        head = left_head
        left_tail.right = root
        root.left = left_tail

    right_head, right_tail = inorder(root.right)

    if right_head:
        root.right = right_head
        right_head.left = root
        tail = right_tail

    return head, tail

def pprint(root):
    while root:
        print root.val
        root = root.right

def test():
    nodes = [TreeNode(i) for i in range(6)]
    nodes[3].left = nodes[1]
    nodes[3].right = nodes[5]
    nodes[1].left = nodes[0]
    nodes[1].right = nodes[2]
    nodes[5].left = nodes[4]

    bst_to_dll(nodes[3])
    pprint(nodes[0])

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


if __name__ == '__main__':
    test()
