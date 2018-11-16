# Path Sum IV
# If the depth of a tree in range [1, 4], value of every node in range [0, 9], and the tree is valid,
# and given a list of ascending three-digits integers representing a binary tree,
# return the sum of all paths from the root towards the leaves.
# f([113, 215, 221]) => 12
#   3
#  / \
# 5   1
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        tree = {}  # position of a node => val
        for num in nums:
            tree[num / 10] = num % 10

        path_sum = [0]
        self.preorder(nums[0] / 10, 0, path_sum, tree)
        return path_sum[0]

    def preorder(self, root, acc_sum, path_sum, tree):
        level = root / 10
        pos = root % 10

        left = (level + 1) * 10 + pos * 2 - 1
        right = left + 1

        acc_sum += tree[root]

        if not left in tree and not right in tree:
            path_sum[0] += acc_sum
            return

        if left in tree:
            self.preorder(left, acc_sum, path_sum, tree)
        if right in tree:
            self.preorder(right, acc_sum, path_sum, tree)
