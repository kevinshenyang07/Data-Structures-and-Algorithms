# ZigZag Conversion
class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if n < 2:
            return s

        rows = [[] for _ in range(n)]
        m = 2 * n - 2  # length of cycles = n + (n - 2)

        for i, char in enumerate(s):
            j = i % m

            if j < n:
                rows[j].append(char)  # straight down
            else:
                rows[m - j].append(char)  # zigzag back

        return ''.join(''.join(row) for row in rows)
# test cases:
# for s = "PAYPALISHIRING":
#   n = 3:
#     P   A   H   N
#     A P L S I I G
#     Y   I   R
#     => "PAHNAPLSIIGYIR"
#   n = 4:
#     P     I    N
#     A   L S  I G
#     Y A   H R
#     P     I
#     => "PINALSIGYAHRPI"
