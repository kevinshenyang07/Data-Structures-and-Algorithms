from __future__ import print_function

class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if self.val <= value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)

    # find the node with target value, starting with a node
    # return None if not found
    def find(self, value):
        if self.val == value:
            return self
        if self.val < value:
            if self.right:
                self.right.find(value)
            else:
                return None
        else:
            if self.left:
                self.left.find(value)
            else:
                return None

    # node has no children, simply remove it
    # node has one child, the child take its place
    # node has two children, find the max on the left or the min on the right
    # return the replacing node
    def delete(self, value):
        if self.val == value:  # target node found
            if self.right and self.left:  # has two children
                # get the successor node and its parent
                psucc, succ = self.right._find_min(self)
                # splice out the successor, since succ is already the min
                # it can only has right child
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                # reset the left and right children of the successor
                succ.left = self.left
                succ.right = self.right
                return succ
            else:  # node child <= 1
                if self.left:
                    return self.left  # promote the left subtree or assign None
                else:
                    return self.right   # promote the right subtree or assign None
        else:
            if self.val < value:
                if self.right:
                    self.right = self.right.delete(value)
                # else the key is not in the tree
            else:
                if self.left:
                    self.left = self.left.delete(value)
                # else the key is not in the tree
        return self

    # helper methods
    def _find_min(self, parent):
        if self.left:
            return self.left._find_min(self)  # self as the parent
        else:
            return [parent, self]

    def __repr__(self):
        return str(self.val)

# values of nodes in left subtree are smaller than root value
# values of nodes in right subtree are greater than root value
class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = TreeNode(value)

    def find(self, value):
        if self.root:
            return self.root.find(value)
        return None

    def delete(self, value):
        if self.root:
            self.root = self.root.delete(value)

    # optional helper methods go here:
    def print_tree(self):
        curr_level = [self.root]
        while curr_level:
            print(curr_level)
            next_level = []
            for ele in curr_level:
                if ele.left:
                    next_level.append(ele.left)
                if ele.right:
                    next_level.append(ele.right)
                curr_level = next_level


if __name__ == '__main__':

    bst = BinarySearchTree()
    for val in [5, 3, 7, 1, 4, 9, 0, 2, 1.5, 10]:
        bst.insert(val)
    bst.print_tree()

    print("deleting 3")
    bst.delete(3)
    bst.print_tree()
    print("deleting 2")
    bst.delete(2)
    bst.print_tree()

    print(inorder(bst.root))
