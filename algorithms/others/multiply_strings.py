# Multiply Strings
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                k = i + j + 1  # index of last digit of mul
                subtotal = mul + res[k]
                # update last and previous digit
                res[k] = subtotal % 10
                res[k - 1] += subtotal / 10

        output = ''.join(str(digit) for digit in res).lstrip('0')
        return output or '0'
# just like how its done manually
#     1 2 3
# x     4 5
# ----------
#       1 5
#     1 0
#     5
#     1 2
#     8
#   4
# ----------
# = 5 5 3 5
#
# index:
#   0 1 2 3
