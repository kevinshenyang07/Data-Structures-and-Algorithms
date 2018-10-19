# Length of Longest Fibonacci Subsequence
# Given a strictly increasing array A of positive integers forming a sequence,
# find the length of the longest fibonacci-like subsequence of A.
# If one does not exist, return 0.
# f([1,2,3,4,5,6,7,8]) => [1,2,3,5,8]
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        dp[i][j]: length of the subseq whose last two elements to be A[i] and A[j]
        dp[i][j] = 2                 for any pair of (A[i], A[j])
                 = dp[k][i] + 1      k being A.index(A[j] - A[i])
        """
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        indices = {}
        res = 0

        for j in range(n):
            indices[A[j]] = j

            for i in range(j):
                k = indices.get(A[j] - A[i], -1)
                # there can be and there is a seq ends with A[j] - A[i]
                if A[i] > A[j] - A[i] and k >= 0:
                    # A[i] can be appended to current subseq
                    dp[i][j] = dp[k][i] + 1
                else:
                    # A[i] and A[j] are the first two elements in the subseq
                    dp[i][j] = 2

                res = max(res, dp[i][j])

        return res if res > 2 else 0
# O(n^2) time and space
