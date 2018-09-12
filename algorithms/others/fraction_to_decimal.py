# Fraction to Recurring Decimal
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return 'NaN'

        sign = '' if numerator * denominator >= 0 else '-'
        X, Y = abs(numerator), abs(denominator)
        left, residual = divmod(X, Y)
        right = ''
        seen = {}  # residual => index of that residual last appeared

        while residual != 0:
            print residual, right, seen
            if residual in seen:
                break
            seen[residual] = len(right)
            digit, residual = divmod(residual * 10, Y)
            right += str(digit)

        left = sign + str(left)

        if not right:
            return left
        elif residual == 0:
            return left + '.' + right
        else:
            r = seen[residual]
            return left + '.' + right[:r] + '(' + right[r:] + ')'
# thought process:
# to get the digits after '.', loop until the residual becomes 0
# or the same residual appears for the second time
