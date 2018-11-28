from binary_indexed_tree import BIT

# Count of Smaller Numbers After Self
class Solution(object):
    def countSmaller(self, nums):
        # num => index in the sorted and deduped nums
        num_to_order = {}
        for i, num in enumerate(sorted(set(nums))):
            num_to_order[num] = i

        tree = BIT(len(num_to_order))  # mapped to ascending order of nums
        counts = [-1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            order = num_to_order[nums[i]]
            # count of the frequencies of appeared numbers with smaller order
            counts[i] = tree.query(order - 1)
            # nums[i] appears once for all nums[j] > nums[i], where j < i
            tree.update(order, 1)

        return counts


# BST node version
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []

        n = len(nums)
        counts = [-1] * n
        counts[-1] = 0
        root = TreeNode(nums[-1])

        for i in range(n - 2, -1, -1):
            # build tree on the fly
            counts[i] = root.insert(TreeNode(nums[i]))

        return counts

# BST version
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.left_size = 0

    def insert(self, val):
        node = TreeNode(val)
        count = 0
        prev = root = self

        while root:
            if root.val < val:
                count += root.count + root.left_size
                prev, root = root, root.right
            elif root.val > val:
                root.left_size += 1
                prev, root = root, root.left
            else:
                root.count += 1
                return count + root.left_size

        if prev.val < val:
            prev.right = node
        else:
            prev.left = node

        return count
# O(nlogn) time in average, but could be O(n^2) if nums == sorted(nums)
