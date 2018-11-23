import random
import collections


# give a list of words as dictionary, and player 1 choose one from it
# use a data structure to reduce
# 1. time to search in dictionary
# 2. times to call guess()
class HangmanGame(object):
    def __init__(self, words):
        self.words = words
        self.picked = None
        self.state = []

    def pick(self):
        self.picked = random.choice(self.words)
        self.state = ['_'] * len(self.picked)

    def guess(self, letter):
        for i, char in enumerate(self.picked):
            if letter == char:
                self.state[i] = char
        return self.state

    def play(self):
        candidates = set(word for word in self.words if len(word) == len(self.state))
        root = self.build_trie()
        guessed = set()

        while '_' in self.state:
            letter = self.choose_letter(candidates, guessed)
            guessed.add(letter)

            print letter, self.guess(letter)
            candidates = self.filter_by(root, candidates)

    def choose_letter(self, candidates, guessed):
        counter = collections.Counter()
        for candidate in candidates:
            for char in candidate:
                if char not in guessed:
                    counter.update(char)
        return counter.most_common(1)[0][0]

    def build_trie(self):
        root = TrieNode()
        for word in self.words:
            curr = root
            for char in word:
                curr.children[char] = curr.children.get(char, TrieNode())
                curr = curr.children[char]
            curr.is_word = True
            curr.data = word
        return root

    def filter_by(self, root, candidates):
        level = [root]

        for char in self.state:
            next_level = []

            for node in level:
                for key, child in node.children.iteritems():
                    if char == '_' or key == char:
                        next_level.append(child)

            level = next_level

        return candidates & set(node.data for node in level)


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.data = ''


if __name__ == '__main__':
    words = ['brown', 'foxes', 'jumps', 'into', 'apple']
    game = HangmanGame(words)
    game.pick()
    game.play()
