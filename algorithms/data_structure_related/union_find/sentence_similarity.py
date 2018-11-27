from union_find import UnionFindWithMap as UnionFind

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

        uf = UnionFind()
        for s1, s2 in pairs:
            uf.union(s1, s2)

        for i in range(len(words1)):
            w1, w2 = words1[i], words2[i]
            if w1 == w2:
                continue
            # ! be careful about conditions when word is not mapping
            if w1 not in uf.parents or w2 not in uf.parents:
                return False
            if uf.find(w1) != uf.find(w2):
                return False

        return True
