from collections import defaultdict


# Sentence Similarity II
# assume if a word does not appear in pairs, it would be not
# be similar to any other words
class Solution(object):
    def are_sentences_similar_2(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        mapping = defaultdict(set)

        # generate edges between nodes (words)
        for w1, w2 in pairs:
            mapping[w1].add(w2)
            mapping[w2].add(w1)

        for i in range(len(words1)):
            w1, w2 = words1[i], words2[i]
            if w1 == w2:
                continue
            if w1 not in mapping or w2 not in mapping:
                return False
            if not self.dfs(w1, w2, mapping, set()):
                return False

        return True

    def dfs(self, source, target, mapping, visited):
        # valid result condition
        if target in mapping[source]:
            return True
        # early stop condition
        if source in visited:
            return False
        # recursion definition
        visited.add(source)
        for adj_word in mapping[source]:
            if self.dfs(adj_word, target, mapping, visited):
                return True

        return False
# O(m * n) time, O(n) space
# m being number of words, n being number of pairs
# improvement: cache found similarity
