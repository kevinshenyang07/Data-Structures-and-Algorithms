# Implement Magic Dictionary
class MagicDictionary(object):

    def __init__(self):
        self.word_set = set()
        self.neighbors = collections.Counter()

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in words:
            self.word_set.add(word)
            for candidate in self.candidates(word):
                self.neighbors[candidate] += 1

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for candidate in self.candidates(word):
            if self.neighbors[candidate] > 1:
                return True
            elif self.neighbors[candidate] == 1 and word not in self.word_set:
                return True
        return False

    def candidates(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i + 1:]
