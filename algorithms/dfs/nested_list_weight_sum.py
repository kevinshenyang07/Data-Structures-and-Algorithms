# Nested List Weight Sum I
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# f([1,[4,[6]]]) => 27 = 1 + 4 * 2 + 6 * 3
class SolutionQ1(object):
    def depthSum(self, nested_list):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.dfs(nested_list, 1)

    def dfs(self, nested_list, depth):
        acc = 0
        for nested in nested_list:
            if nested.isInteger():
                acc += nested.getInteger() * depth
            else:
                acc += self.dfs(nested.getList(), depth + 1)
        return acc


# Nested List Weight Sum II
# This time the weight is defined from bottom up, which means root has largest weight.
# f([1,[4,[6]]]) => 17 = 1 * 3 + 4 * 2 + 6 * 1
# approach:            = (1 + 4 + 6) * 4 - (1 * 1 + 4 * 2 + 6 * 3)
class SolutionQ2(object):
    def depthSumInverse(self, nested_list):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.max_depth = 0
        self.flat_sum = 0
        acc_sum = self.dfs(nested_list, 1)
        return self.flat_sum * (self.max_depth + 1) - acc_sum

    # still accumulate by original weights
    def dfs(self, nested_list, depth):
        acc = 0
        for nested in nested_list:
            if nested.isInteger():
                self.max_depth = max(self.max_depth, depth)
                self.flat_sum += nested.getInteger()
                acc += nested.getInteger() * depth
            else:
                acc += self.dfs(nested.getList(), depth + 1)
        return acc


# # interface:
# class NestedInteger(object):
#     def __init__(self, value=None):
#         """
#         If value is not specified, initializes an empty list.
#         Otherwise initializes a single integer equal to value.
#         """
#
#     def isInteger(self):
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         :rtype bool
#         """
#
#     def add(self, elem):
#         """
#         Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#         :rtype void
#         """
#
#     def setInteger(self, value):
#         """
#         Set this NestedInteger to hold a single integer equal to value.
#         :rtype void
#         """
#
#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """
#
#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """