# Decode String
# assume the expression is valid and only alphabets are repeated
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[1, '']]  # repeat curr_n, pattern
        curr_n = 0

        for i, char in enumerate(s):
            if char.isdigit():
                curr_n = 10 * curr_n + int(char)
                if not s[i + 1].isdigit():  # number cannot be the last char
                    stack.append([curr_n, ''])
                    curr_n = 0
            elif char == '[':
                continue
            elif char == ']':
                # !!avoid overwriting curr_n with n
                n, pattern = stack.pop()
                repeated = n * pattern
                stack[-1][1] = stack[-1][1] + repeated
            else:
                stack[-1][1] = stack[-1][1] + char

        return stack[0][1]
