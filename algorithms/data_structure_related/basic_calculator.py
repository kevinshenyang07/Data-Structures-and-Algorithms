# Basic Calculator
# assumption: the expression is valid, integers are non-negative
# may have white space
class Solution(object):
    def calculate(self, s):
        stack = [[]]  # for s that starts without "("
        num = 0
        for i, char in enumerate(s):
            if char == ' ':
                continue
            elif char == '(':
                stack.append([])
            elif char == ')':
                subtotal = self.calc(stack.pop())
                stack[-1].append(subtotal)
            elif char in '+-':
                stack[-1].append(char)
            elif char.isdigit():
                num = 10 * num + int(char)
                if i == len(s) - 1 or not s[i + 1].isdigit():
                    stack[-1].append(num)
                    num = 0

        return self.calc(stack[-1])

    def calc(self, elements):
        res = 0
        sign = 1
        for element in elements:
            if isinstance(element, int):
                res += sign * element
            else:
                sign = 1 if element == '+' else -1
        return res
# test cases:
# '()' => 0
# '2-(5-6)' => 3


# Basic Calculator II
# assumption: the expression is valid, there won't be expr like 5/-2
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []  # stack[-1]: a
        operator = '+'
        num = 0  # b

        for i, char in enumerate(s):
            if char == ' ':
                continue
            elif char in '+-*/':
                operator = char
            else:
                num = 10 * num + int(char)
                if i == len(s) - 1 or not s[i + 1].isdigit():
                    if operator == '+':
                        stack.append(num)
                    elif operator == '-':
                        stack.append(-num)
                    elif operator == '*':
                        stack.append(stack.pop() * num)
                    elif operator == '/':
                        # divide negative number gets rounded down: -4 / 3 == -2
                        a = stack.pop()
                        sign = 1 if a >= 0 else -1
                        stack.append(sign * (abs(a) / num))
                    num = 0

        res = 0
        while stack:
            res += stack.pop()
        return res
