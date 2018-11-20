# K-Similar Strings
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        queue = collections.deque()
        queue.append((A, 0))
        visited = set([A])

        while queue:
            word, swaps = queue.popleft()

            if word == B:
                return swaps

            for next_word in self.next_words(word, B):
                if next_word not in visited:
                    queue.append((next_word, swaps + 1))
                    visited.add(next_word)

        return -1

    def next_words(self, word, target):
        chars = list(word)
        words = []
        # skip the chars already matched
        i = 0
        while word[i] == target[i]:
            i += 1
        # only make a swap when it makes A more similar to B
        for j in range(i + 1, len(word)):
            if chars[j] == target[i]:
                chars[i], chars[j] = chars[j], chars[i]
                words.append(''.join(chars))
                chars[i], chars[j] = chars[j], chars[i]
        return words
