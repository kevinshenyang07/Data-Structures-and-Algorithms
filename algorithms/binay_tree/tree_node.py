class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class TreeNaryNode(object):
    def __init__(self, x, childlren):
        self.val = x
        self.childlren = childlren
