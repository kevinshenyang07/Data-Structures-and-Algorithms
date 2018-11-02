# find string matching from stream
# given a char stream with two APIs next() and hasNext(), and words List[str] as target
# whenever a target word appears in the stream, print it out
# Approach:
# build a trie from last char to first char, and keep track of chars read from stream
# whenever a new char comes in traverse down the trie to find matches
class Stream(object):
    def __init__(self, chars):
        self.chars = chars
        self.i = 0

    def next(self):
        char = self.chars[self.i]
        self.i += 1
        return char

    def has_next(self):
        return self.i < len(self.chars)


class TrieNode(object):
    def __init__(self):
        self.parent = {}
        self.is_start = False
        self.data = None


class WordLogger(object):
    def __init__(self, words):
        self.root = self.build_trie(words)

    def build_trie(self, words):
        root = TrieNode()

        for word in words:
            curr = root
            for i in range(len(word) - 1, -1, -1):
                char = word[i]
                curr.parent[char] = curr.parent.get(char, TrieNode())
                curr = curr.parent[char]
            curr.is_start = True
            curr.data = word

        return root

    def find_matched(self, stream):
        chars = []
        while stream.has_next():
            chars.append(stream.next())

            i = len(chars) - 1
            curr = self.root
            while i >= 0 and chars[i] in curr.parent:
                curr = curr.parent[chars[i]]
                i -= 1
                if curr.is_start:
                    print curr.data


if __name__ == '__main__':
    stream = Stream('aabcate')
    logger = WordLogger(['cat', 'aabcat', 'cate'])
    logger.find_matched(stream)
