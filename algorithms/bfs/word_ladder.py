# Word Ladder
class Solution(object):
    def ladderLength(self, begin_word, end_word, word_list):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(word_list)
        queue = collections.deque()
        queue.append((begin_word, 1))

        while queue:
            word, dist = queue.popleft()
            if word == end_word:
                return dist
            for next_word in self.next_words(word, word_set):
                queue.append((next_word, dist + 1))

        return 0

    def next_words(self, word, word_set):
        words = []
        for i in range(len(word)):
            for char in string.lowercase:
                next_word = word[:i] + char + word[i+1:]
                # once a valid next_word is found it must be on a shortest path
                # so we can greedily remove it word_set
                if next_word != word and next_word in word_set:
                    words.append(next_word)
                    word_set.remove(next_word)
        return words
