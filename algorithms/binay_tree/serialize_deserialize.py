from tree_node import TreeNode, TreeNaryNode

# approach:
# use preorder to encode then iterator to decode
# use '#' to indicate end of traversal under current node

# Serialize and Deserialize Binary Tree
class CodecQ1(object):
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
class CodecQ2(object):
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
