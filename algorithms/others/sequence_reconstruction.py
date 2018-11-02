# Sequence Reconstruction
# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
# The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104.
# Reconstruction means building a shortest common supersequence of the sequences in seqs
# (i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
# Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not any(seqs):
            return False

        n = len(org)
        pos = { org[i] : i for i in range(n) }
        matched = [False] * (n + 1)
        to_match = n - 1  # the last number in org is not deducted

        for seq in seqs:
            for i in range(len(seq)):
                # node out of range
                if seq[i] < 1 or seq[i] > n:
                    return False
                if i == 0:
                    continue

                u, v = seq[i - 1], seq[i]
                # u is after v in org
                if pos[u] >= pos[v]:
                    return False
                # otherwise mark u to be matched if any pair of (u, v) occurs in org
                if pos[u] + 1 == pos[v] and not matched[u]:
                    matched[u] = True
                    to_match -= 1

        return to_match == 0
# test cases:
# org: [1,2,3], seqs: [[1,2],[1,3]] => False
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]] => True
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]] => True
