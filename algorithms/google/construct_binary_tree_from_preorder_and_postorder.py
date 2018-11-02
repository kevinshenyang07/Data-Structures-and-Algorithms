# need to make assumption that if a node has right child, it must have left child
# otherwise we don't know if the first child of a parent is on the left or right
# e.g. a preorder as [1,2,3,4,5], we don't know 2 is left child or not
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        self.pre_map = {}
        for i, val in enumerate(pre):
            self.pre_map[val] = i

        self.post_map = {}
        for i, val in enumerate(post):
            self.post_map[val] = i

        return self.helper(pre, post, 0, len(post) - 1)

    def helper(self, pre, post, i, j):
        if i > j:
            return None
        if i == j:
            return TreeNode(post[j])

        root_val = post[j]
        root_idx = self.pre_map[root_val]
        root = TreeNode(root_val)
        # root_idx == n - 1 will be handled in the second base case
        left_val = pre[root_idx + 1]
        left_idx = self.post_map[left_val]

        root.left = self.helper(pre, post, i, left_idx)
        root.right = self.helper(pre, post, left_idx + 1, j - 1)

        return root
# pre = [1, 2, 4, 8, 9, 5, 3, 6, 7]
# post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
# => root to be 1, its left child must be 2
# => divide sub-trees by [8, 9, 4, 5, 2] and [6, 7, 3]
# and so on
# O(n) time and space