# Integer To English Words
# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def helper(num):
            million = 1000000
            billion = million * 1000
            res = ''

            if num >= billion:
                res = helper(num / billion) + ' Billion ' + helper(num % billion)
            elif num >= million:
                res = helper(num / million) + ' Million ' + helper(num % million)
            elif num >= 1000:
                res = helper(num / 1000) + ' Thousand ' + helper(num % 1000)
            elif num >= 100:
                res = helper(num / 100) + ' Hundred ' + helper(num % 100)
            elif num >= 20:
                res = tens[num / 10] + ' ' + helper(num % 10)
            else:
                res = below_tweenty[num]

            return res.strip()

        if num == 0:
            return "Zero"

        below_tweenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        return helper(num)

# Examples:
# f(123) => "One Hundred Twenty Three"
# f(12345) => "Twelve Thousand Three Hundred Forty Five"
# f(1234567) => "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# f(1234567891) => "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

# Thought process
# 1. get boundary: 2147483647 (~ 2 billion), so the maximum scale is Billion
# 2. base cases: <20, < 100
# 3. determine rule: f(n) = f(n / scale) + ' Scale ' + f(n % scale)


if __name__ == '__main__':
    solution = Solution()
    print solution.numberToWords(0)
    print solution.numberToWords(10)
    print solution.numberToWords(12)
    print solution.numberToWords(50)
    print solution.numberToWords(1234567)
    print solution.numberToWords(1234567890)
