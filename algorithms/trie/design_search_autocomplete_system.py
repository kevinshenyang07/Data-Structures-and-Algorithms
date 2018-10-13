from collections import deque

# Design Search Autocomplete System
# since it's locked and long, description refer to http://www.cnblogs.com/grandyang/p/7897166.html
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.data = None
        self.freq = 0

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = TrieNode()
        self.keyword = ''
        for i, sentence in enumerate(sentences):
            self.add_sentence(sentence, times[i])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        res = []
        if c != '#':
            self.keyword += c
            candidates = self.search(self.keyword)
            res = [c.data for c in sorted(candidates, key=lambda c: (-c.freq, c.data))][:3]
        else:
            self.add_sentence(self.keyword, 1)
            self.keyword = ''
        return res

    def add_sentence(self, s, freq):
        curr = self.trie
        for char in s:
            curr.children[char] = curr.children.get(char, TrieNode())
            curr = curr.children[char]

        curr.is_word = True
        curr.data = s
        curr.freq += freq

    # do not use heap since it won't cover cases when two sentences
    # have the same frequency and need to output in alphabetical order
    def search(self, s):
        curr = self.trie
        for char in s:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        res = []
        queue = deque([curr])

        while queue:
            node = queue.popleft()

            if node.is_word:
                res.append(node)
            for nbr in node.children.values():
                queue.append(nbr)

        return res
