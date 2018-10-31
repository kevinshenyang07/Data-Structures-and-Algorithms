from tree_node import TreeNode, TreeNaryNode

# approach:
# use preorder to encode then iterator / queue to decode
# use '#' to indicate end of traversal under current node

# Serialize and Deserialize Binary Tree
class Codec(object):
    def serialize(self, node):
        if not node:
            return '#'

        left = self.serialize(node.left)
        right = self.serialize(node.right)

        return ' '.join([str(node.val), left, right])

    def deserialize(self, data):
        return self.build_tree(iter(data.split(' ')))

    def build_tree(self, it):
        frag = next(it)
        if frag == '#':
            return None

        root = TreeNode(int(frag))
        root.left = self.build_tree(it)
        root.right = self.build_tree(it)
        return root


# Serialize and Deserialize N-ary Tree
class Codec(object):
    def serialize(self, root):
        if not root:
            return '#'

        children_s = []
        for child in root.children:
            children_s.append(self.serialize(child))
        children_s.append('#')

        return ' '.join([str(root.val)] + children_s)

    def deserialize(self, data):
        return self.build_tree(iter(data.split(' ')))

    def build_tree(self, it):
        frag = next(it)
        if frag == '#':
            return None

        root = Node(int(frag), [])
        # until all nodes under root has been visited
        while True:
            child = self.build_tree(it)
            if not child:
                break
            root.children.append(child)
        return root


# Serialize and Deserialize BST
class Codec:
    def serialize(self, root):
        visited = []
        self.preorder(root, visited)
        return ' '.join(str(v) for v in visited)

    def preorder(self, root, visited):
        if root:
            visited.append(root.val)
            self.preorder(root.left, visited)
            self.preorder(root.right, visited)

    def deserialize(self, data):
        if not data:
            return []

        queue = collections.deque(int(v) for v in data.split(' '))
        return self.build_tree(queue, float('-inf'), float('inf'))

    def build_tree(self, queue, min_val, max_val):
        # every node on the left should be smaller than val, and vice versa
        if queue and min_val < queue[0] < max_val:
            val = queue.popleft()
            node = TreeNode(val)

            node.left = self.build_tree(queue, min_val, val)
            node.right = self.build_tree(queue, val, max_val)

            return node
