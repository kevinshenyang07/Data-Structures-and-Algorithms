from binary_indexed_tree import BIT

# Count of Smaller Numbers After Self
class Solution(object):
    def countSmaller(self, nums):
        # num => index in the sorted and deduped nums
        num_to_order = {}
        for i, num in enumerate(sorted(set(nums))):
            num_to_order[num] = i

        tree = BIT(len(num_to_order))  # mapped to ascending order of nums
        counts = []

        for i in range(len(nums) - 1, -1, -1):
            order = num_to_order[nums[i]]
            # count of the frequencies of appeared numbers with smaller order
            counts.append(tree.query(order - 1))
            # nums[i] appears once for all nums[j] > nums[i], where j < i
            tree.update(order, 1)

        return counts[::-1]
