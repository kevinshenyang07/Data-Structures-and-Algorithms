# Decode String
# assume the expression is valid and only alphabets are repeated
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[1, '']]  # repeat curr_num, pattern
        curr_num = 0

        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = 10 * curr_num + int(char)
            elif char == '[':
                stack.append([curr_num, ''])
                curr_num = 0
            elif char == ']':
                times, pattern = stack.pop()
                stack[-1][1] += times * pattern
            else:
                stack[-1][1] += char

        return stack[0][1]
