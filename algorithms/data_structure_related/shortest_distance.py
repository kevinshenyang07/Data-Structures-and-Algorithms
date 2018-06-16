# Shortest Word Distance

# v1
# assumption: word1 != word2, word1 and word2 are in the list
def shortest_distance_1(words, word1, word2):
    ans = float('inf')
    p1 = p2 = -1

    for i, word in enumerate(words):
        if word == word1:
            p1 = i
        if word == word2:
            p2 = i
        # all p1 only need to be compared by nearby p2, vice versa
        if p1 != -1 and p2 != -1:
            ans = min(ans, abs(p1 - p2))

    return ans
# O(n) time, O(1) space


# v2
# shortest() will be called many times with different params
# ask interviewer: is the number of shortest() calls larger than the size of words?
#            true: O(n^2) for __init__(), O(1) for shortest()
#           false: O(n) for __init__(), O(n) for shortest()
class WordDistance(object):

    def __init__(self, words):
        self.indices = {}

        for i, word in enumerate(words):
            self.indices[word] = self.indices.get(word, []) + [i]


    def shortest(self, word1, word2):
        ans = float('inf')
        indices1, indices2 = self.indices[word1], self.indices[word2]
        i = j = 0

        while i < len(indices1) and j < len(indices2):
            ans = min(ans, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1

        return ans
# O(n) time for __init__(), O(n) for shortest()


# v3
# word1 can be the same as word2
def shortest_distance_3(words, word1, word2):
    ans = float('inf')
    p1 = p2 = -1

    for i, word in enumerate(words):
        if word == word1:
            p1 = p2 if word1 == word2 else i
        if word == word2:
            p2 = i
        # all p1 only need to be compared by nearby p2, vice versa
        if p1 != -1 and p2 != -1:
            ans = min(ans, abs(p1 - p2))

    return ans
# O(n) time, O(1) space
