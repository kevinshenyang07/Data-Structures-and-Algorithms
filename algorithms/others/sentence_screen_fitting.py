# Sentence Screen Fitting
class SolutionV1(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        n = len(s)
        used = 0  # number of chars used in the joined sentence

        for _ in range(rows):
            used += cols
            # step back until a space is found
            # can be slow when the next word is long
            while s[used % n] != ' ':
                used -= 1
            # until now used is the index of last space
            # move to the first char of next word
            used += 1

        return used / n
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

# improvement with cache
class SolutionV2(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        n = len(s)

        # steps needed to go back to the first char of the word
        steps_back = [0] * n
        first = 0
        for i in range(n):
            if s[i] == ' ':
                first = i + 1
            steps_back[i] = i - first

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
# steps_back = [0, 1, -1, 0, 1, 2, -1, 0, -1]
# O(r) time, O(n * w) space
