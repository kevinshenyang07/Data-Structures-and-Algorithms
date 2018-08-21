# Decode String
# assume the expression is valid and only alphabets are repeated
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        curr_n = 0

        for i, char in enumerate(s):
            if char in '0123456789':
                curr_n = 10 * curr_n + int(char)
            elif char == '[':
                stack.append(['', curr_n])
                curr_n = 0
            elif char == ']':
                # be careful about using the same variable name for curr_n and n
                substr, n = stack.pop()
                repeated = substr * n
                stack[-1][0] = stack[-1][0] + repeated
            else:
                stack[-1][0] = stack[-1][0] + char

        return stack[0][0]
# Note:
# 1. backets can be nested like 3[a2[b]]
# 2. number could have more than 1 digit
