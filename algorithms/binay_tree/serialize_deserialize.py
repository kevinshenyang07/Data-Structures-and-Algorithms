from tree_node import TreeNode


# Serialize and Deserialize Binary Tree
class Codec(object):
    def serialize(self, node):
        if not node:
            return 'null'
        left = self.serialize(node.left)
        right = self.serialize(node.right)
        return ','.join(str(node.val), left, right)

    def deserialize(self, data):
        return self.build_tree(iter(data.split(',')))

    def build_tree(self, val_iterator):
        val = next(val_iterator)
        if val == 'null':
            return None
        node = TreeNode(val)
        node.left = self.build_tree(val_iterator)
        node.right = self.build_tree(val_iterator)
        return node
