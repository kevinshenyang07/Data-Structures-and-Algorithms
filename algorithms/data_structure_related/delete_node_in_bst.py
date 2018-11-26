# Delete Node in a BST
# iterative is very error-prone
class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif not root.left:
            node_right = root.right
            root.right = None
            return node_right
        elif not root.right:
            node_left = root.left
            root.left = None
            return node_left
        else:
            successor = self.largest(root.left)
            root.val = successor.val
            # don't forget to remove the successor (which has the same requirement)
            root.left = self.deleteNode(root.left, successor.val)
        return root

    def largest(self, node):
        while node.right:
            node = node.right
        return node
# O(height of tree) time, O(1) space