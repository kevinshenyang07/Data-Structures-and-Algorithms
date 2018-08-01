# Ternary Expression Parser
# Given a string representing arbitrarily nested ternary expressions,
# calculate the result of the expression.
# You can always assume that the given expression is valid and only consists of
# digits 0-9, ?, :, T and F (T and F represent True and False respectively).
# f("F?1:T?4:5") => "4"
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ""

        stack = []
        for i in range(len(expression) - 1, -1, -1):
            char = expression[i]
            if stack and stack[-1] == '?':
                stack.pop()  # pop "?"
                left = stack.pop()
                stack.pop()  # pop ":"
                right = stack.pop()

                if char == 'T':
                    stack.append(left)
                else:
                    stack.append(right)
            else:
                stack.append(char)

        return stack[-1]
# Note:
# 1. Each number will contain only one digit.
# 2. The condition will always be either T or F. That is, the condition will never be a digit.
# 3. T/F can also be return values.
