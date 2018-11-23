# Evaluate Reverse Polish Notation
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = '+-*/'

        for token in tokens:
            # do not use token.isdigit() first since
            # '-11' will be evaludated as False
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.apply_operator(a, b, token))
            else:
                stack.append(int(token))

        return stack.pop()

    def apply_operator(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            # 6 / (-132) will be evaludated as -1 in Py2
            # handle it differently
            sign = 1 if a * b > 0 else -1
            divided = abs(a) / abs(b)
            return sign * divided
