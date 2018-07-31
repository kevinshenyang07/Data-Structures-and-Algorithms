# Valid Word Square
# Given a sequence of words, check whether it forms a valid word square.
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]
# => true
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            # need to start from 0 instead of i + 1
            # since there could be extra chars before i + 1 not being checked
            for j in range(len(words[i])):
                # for words[j][i], if not in range or char not equal
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False

        return True
