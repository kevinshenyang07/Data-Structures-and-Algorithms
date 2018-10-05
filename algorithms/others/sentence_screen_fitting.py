# Sentence Screen Fitting
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        used = 0  # chars used in the joined sentence

        for i in range(rows):
            used += cols
            # step back until a space is found
            while s[used % len(s)] != ' ':
                used -= 1
            # next char must not be a space
            used += 1

        return used / len(s)
# sentence = ["ab", "cde", "f"]
# s = "ab cde f "
# rows = 5, cols = 4
#
# ab cde f ab cde f ab cde f...
# xxx
#    xxxx
#        xxxxx
#             xxxx
#                 xxxxx
# => (3 + 4 + 5 + 4 + 5) / 9 = 2
#
# O(r * w) time, O(n * w) space
# r being rows, w being word length, n being
