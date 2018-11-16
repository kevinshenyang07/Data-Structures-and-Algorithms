# Integer To English Words
# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def translate(num):
            if num < 20:
                res = BELOW_TWEENTY[num]
            elif num < 100:
                res = TENS[num / 10] + ' ' + BELOW_TWEENTY[num % 10]
            elif num < 1000:
                res = translate(num / 100) + ' Hundred ' + translate(num % 100)
            elif num < MILLION:
                res = translate(num / 1000) + ' Thousand ' + translate(num % 1000)
            elif num < BILLION:
                res = translate(num / MILLION) + ' Million ' + translate(num % MILLION)
            else:
                res = translate(num / BILLION) + ' Billion ' + translate(num % BILLION)
            return res.strip()

        # leetcode does not support Python class variable, thus enclosing here
        BELOW_TWEENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        MILLION = 1000000
        BILLION = MILLION * 1000
        # only for original num to be 0
        if num == 0:
            return 'Zero'
        return translate(num)

# Examples:
# f(123) => "One Hundred Twenty Three"
# f(12345) => "Twelve Thousand Three Hundred Forty Five"
# f(1234567) => "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# f(1234567891) => "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

# Thought process:
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
