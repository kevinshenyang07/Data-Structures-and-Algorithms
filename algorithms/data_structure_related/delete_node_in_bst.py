# Delete Node in a BST
class Solution(object):
    def delete_node(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if not root.left:
                node_right = root.right
                root.right = None
                return node_right
            if not root.right:
                node_left = root.left
                root.left = None
                return node_left
            node_min = self.find_min(root.right)
            root.val = node_min.val
            root.right = self.delete_node(root.right, node_min.val)
        return root

    def find_min(self, root):
        while root.left:
            root = root.left
        return root
# O(height of tree) time, O(1) space