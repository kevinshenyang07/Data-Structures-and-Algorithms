# Similar RGB Color
# example: f("#09f166") => "#11ee66"
# every digit of input is hexadecimal, every two letters represent r/g/b dolor
# find the colors that are closest to original color
class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        if not color or color[0] != '#' or len(color) != 7:
            return ''

        c1, c2, c3 = color[1:3], color[3:5], color[5:]
        return '#' + self.closest(c1) + self.closest(c2) + self.closest(c3)

    def closest(self, c):
        if c[0] == c[1]: return c

        mapping = '0123456789abcdef'
        # 'b3' => chose from 'aa', 'bb', 'cc'
        idx = int(c[0], 16)
        lower = max(idx - 1, 0)
        upper = min(idx + 1, 15)

        min_diff = float('inf')
        res = None

        for i in range(lower, upper + 1):
            num = mapping[i] * 2
            diff = abs(int(c, 16) - int(num, 16))
            if diff < min_diff:
                min_diff = diff
                res = num

        return res
