# H-Index
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        buckets = [0] * (n + 1)

        for citation in citations:
            i = min(citation, n)
            buckets[i] += 1

        num_papers = 0  # how many papers has h+ citations
        for i in range(n, -1, -1):
            num_papers += buckets[i]
            if num_papers >= i:
                return i

        return 0
# given n papers, create n + 1 buckets (last bucket for papers with n+ citations)
# buckets[i]: how many papers have i citations
# [3, 0, 6, 1, 5]
# [1, 1, 0, 1, 0, 2]
#                 <-
#                 2 papers have 5+ citations
#           3 papers have 3+ citations
