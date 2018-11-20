# Solve the Equation
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        a1, b1 = self.get_coefficients(left)
        a2, b2 = self.get_coefficients(right)

        a, b = a1 - a2, b2 - b1  # ax = b

        if a == 0:
            if b == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x={}".format(b / a)

    def get_coefficients(self, s):
        a = b = 0
        sign = 1
        i = j = 0

        while i < len(s):
            if s[i] == '+':
                sign = 1
                i += 1
            elif s[i] == '-':
                sign = -1
                i += 1
            else:
                j = i
                while j < len(s) and s[j] not in '+-':
                    j += 1
                token = s[i:j]
                if token == 'x':
                    a += sign
                elif token[-1] == 'x':
                    a += sign * int(token[:-1])
                else:
                    b += sign * int(token)
                i = j

        return a, b
