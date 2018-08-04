# Valid Word Abbreviation
# f('internationalization', 'i12iz4n') => true
# f('apple', 'a2e') => false
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            # the number cannot start with 0
            if abbr[j] not in '123456789':
                return False

            skip = 0
            while j < len(abbr) and abbr[j] in '0123456789':
                skip = 10 * skip + int(abbr[j])
                j += 1
            i += skip

        return i == len(word) and j == len(abbr)
