# 已知screen的高和宽，给你最小和最大的fontSize，要求给定一个string，将string用尽可能大的
# fontSize显示在screen里。字符串如果是句子的话，单词不能被截断，要分配到下一行。
# 已知两个API getHeight(int fontSize), getWidth(char c, int fontSize)，可以得到每个character在不同fontSize下的高和宽。
# 可以将屏幕按照font的宽高换算成有多少rows * cols，然后用Sentence Screen Fitting的思路判断是否能装下一个字符串或者句子。
# 上面这个作为binary search的条件，最终锁定满足条件的最大字体。（应该是返回right index）
class Solution(object):
    def get_largest_font(self, s, H, W, font_lo, font_hi):
        """
        s: sentence
        H: screen height
        W: screen width
        font_lo: smallest possible font
        font_hi: largest possible font
        """
        while font_lo + 1 < font_hi:
            font_mid = font_lo + (font_hi - font_lo) / 2
            if self.can_fit(s, H, W, font_mid):
                font_lo = font_mid
            else:
                font_hi = font_mid

        if self.can_fit(s, H, W, font_hi):
            return font_hi
        elif self.can_fit(s, H, W, font_lo):
            return font_lo
        else:
            return -1

    # a word can be split into multiple rows
    def can_fit(self, s, H, W, font):
        total_rows = H / getHeight(font)
        rows = 1
        width = 0

        for char in s:
            w = getWidth(char, font)
            width += w

            if width > W:
                width = w
                rows += 1

            if rows > total_rows:
                return False

        return True

    # a word cannot be split into multiple rows
    def can_fit(self, s, H, W, font):
        total_rows = H / getHeight(font)
        rows = 1
        width = 0
        i = 0
        words = s.split(' ')

        while i < len(words):
            w = sum(getWidth(char, font) for char in words[i])
            width += w

            if width + getWidth(' ', font) <= W:
                width += getWidth(' ', font)

            if width > W:
                width = w
                rows += 1

            # a word that cannot fit into any rows
            if w > W:
                return False
            if rows > total_rows:
                return False

            i += 1

        return True
