# Basic Calculator
import string

# assumption: the expression is valid, integers are non-negative
# may have white space
class Solution(object):
    def calculate(self, s):
        stack = [[]]  # for s that starts without "("
        num = 0
        for char in s:
            if char == '(':
                stack.append([])
            elif char == ')':
                stack[-1].append(num)
                num = self.calc(stack.pop())
            elif char in '+-':
                stack[-1].append(num)
                num = 0
                stack[-1].append(char)
            elif char in string.digits:
                num = 10 * num + int(char)

        stack[-1].append(num)  # add last number
        return self.calc(stack[-1])

    def calc(self, elements):
        ans, sign = 0, 1
        sign = 1

        for element in elements:
            if isinstance(element, int):
                ans += sign * element
            else:
                sign = 1 if element == '+' else -1

        return ans