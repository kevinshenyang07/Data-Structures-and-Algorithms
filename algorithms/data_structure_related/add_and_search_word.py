# Add and Search Word
# Design a data structure that supports the following two operations:
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or '.'.
# A '.' means it can represent any one letter.
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_from(word, 0, self.root)

    def search_from(self, word, i, curr):
        # stop condition
        if not word: return False
        # end condition
        if len(word) <= i: return curr.is_word
        # dfs on all children or that char
        char = word[i]
        if char == '.':
            for c in curr.children:
                if self.search_from(word, i + 1, curr.children[c]):
                    return True
        elif char in curr.children:
            if self.search_from(word, i + 1, curr.children[char]):
                return True
        return False
