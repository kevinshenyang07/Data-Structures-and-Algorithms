from union_find import UnionFind

# Sentence Similarity II
# Note: cannot use union find if similarity is not symmetric (has direction)
# (A -> B and A -> C does not mean B -> C)
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        mapping = self.create_mapping(pairs)
        uf = UnionFind(len(mapping))

        for s1, s2 in pairs:
            uf.union(mapping[s1], mapping[s2])

        for i in range(len(words1)):
            w1, w2 = words1[i], words2[i]
            # ! be careful about conditions when word is not mapping
            if w1 == w2:
                continue
            if w1 not in mapping or w2 not in mapping:
                return False
            if uf.find(mapping[w1]) != uf.find(mapping[w2]):
                return False

        return True

    def create_mapping(self, pairs):
        mapping = {}
        idx = 0
        for s1, s2 in pairs:
            if s1 not in mapping:
                mapping[s1] = idx
                idx += 1
            if s2 not in mapping:
                mapping[s2] = idx
                idx += 1
        return mapping
