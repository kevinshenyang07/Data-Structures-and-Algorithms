from tree_node import TreeNode

# Construct Binary Tree from String
# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
# The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
# f("4(2(3)(1))(6(5))")
# =>   4
#    /   \
#   2     6
#  / \   /
# 3   1 5
# Note:
# 1. There will only be '(', ')', '-' and '0' ~ '9' in the input string.
# 2. An empty tree is represented by "" instead of "()".
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        # assume input string is valid
        # assume no calculations in the expression
        dummy = TreeNode(-1)
        stack = [dummy]
        prev = 0
        sign = 1

        for i, char in enumerate(s):
            if char == '-':
                sign = -1
            elif char in '0123456789':
                prev = prev * 10 + int(char)
                # node creation ready
                if i == len(s) - 1 or s[i + 1] in '()':
                    num = sign * prev
                    node = TreeNode(num)
                    prev = 0
                    sign = 1
                    # append node from left to right
                    parent = stack[-1]
                    if not parent.left:
                        parent.left = node
                    elif not parent.right:
                        parent.right = node
                    # node is now the direct parent of next node
                    stack.append(node)
            elif char == ')':
                stack.pop()

        return dummy.left
