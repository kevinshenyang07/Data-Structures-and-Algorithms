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
        num = 0
        is_x = False

        for i, char in enumerate(s):
            if char == 'x':
                if i == 0 or s[i - 1] in '+-':
                    num = 1
                # and "0x" works by default
                is_x = True
            elif char in '0123456789':
                num = 10 * num + int(char)
            else:
                if is_x:
                    a += sign * num
                else:
                    b += sign * num
                # reset
                if char == '+':
                    sign = 1
                else:
                    sign = -1
                num = 0
                is_x = False
        # add up the last token
        if is_x:
            a += sign * num
        else:
            b += sign * num

        return a, b
