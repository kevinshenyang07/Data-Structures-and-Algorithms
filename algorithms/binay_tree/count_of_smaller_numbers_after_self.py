# Count of Smaller Numbers After Self
# build BST from the end, update nodes and get result on each insert
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1  # when val is already in the tree, increment count instead
        self.left_tree_size = 0  # how many child nodes on the left

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert_to(self, node, val):
        if not self.root:
            self.root = TreeNode(val)
            return 0

        if node.val == val:
            node.count += 1
            return node.left_tree_size

        # on the left
        if val < node.val:
            node.left_tree_size += 1

            if not node.left:
                node.left = TreeNode(val)
                return 0
            else:
                return self.insert_to(node.left, val)

        # on the right
        if not node.right:
            node.right = TreeNode(val)
            return node.count + node.left_tree_size
        else:
            return node.count + node.left_tree_size + self.insert_to(node.right, val)


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tree = BinarySearchTree()
        res = []

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            cnt = tree.insert_to(tree.root, num)
            res.append(cnt)

        return res[::-1]


