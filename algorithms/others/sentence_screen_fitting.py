# Sentence Screen Fitting
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        n = len(s)

        # steps needed to go back to the first char of the next word
        # if s[i] != ' ', then s[pos_first:?] will not be used in current row
        steps_back = [0] * n
        pos_first = 0
        for i in range(n):
            if s[i] == ' ':
                pos_first = i + 1  # actually taking a step forward to next char
            steps_back[i] = i - pos_first

        # index of the first char in next word => number of chars used overall
        pos = 0
        for _ in range(rows):
            pos += cols
            pos -= steps_back[pos % n]

        return pos / n
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
# => steps_back = [0, 1, -1, 0, 1, 2, -1, 0, -1]
# => times = (3 + 4 + 5 + 4 + 5) / 9 = 2
#
# O(r) time, O(n * w) space
# r being rows, w being word length, n being
