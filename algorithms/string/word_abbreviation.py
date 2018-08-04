# Word Abbreviation
# visualization https://www.youtube.com/watch?v=yAQMcGY4c90
# assume no duplicates in words, all words have length > 1
class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        prefix_lens = [1] * len(words)
        abbrs = [self.abbreviate(word, 1) for word in words]

        for i in range(len(words)):
            while True:
                dups = set()
                for j in range(i + 1, len(words)):
                    if abbrs[i] == abbrs[j]:
                        dups.add(j)

                if not dups:
                    break

                dups.add(i)
                for idx in dups:
                    prefix_lens[idx] += 1
                    abbrs[idx] = self.abbreviate(words[idx], prefix_lens[idx])

        return abbrs

    def abbreviate(self, word, k):
        if k + 2 >= len(word):
            return word
        else:
            return word[0:k] + str(len(word) - 1 - k) + word[-1]
# O((m * n) ^ 2) time (think worst case that prefix extend to the end)
# m being average length of words, n being number of words
