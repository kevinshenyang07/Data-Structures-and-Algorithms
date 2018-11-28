# Minimum Swaps To Make Sequences Increasing
class Solution(object):
    def minSwap(self, A, B):
        # since it's guaranteed to have a valid answer,
        # only two relationships need to be tracked
        # min swaps to keep A, B increasing in range [0, i]
        n = len(A)
        swap = [n] * n  # while swapping A[i] with B[i]
        no_swap = [n] * n  # while not swapping A[i] with B[i]

        swap[0] = 1
        no_swap[0] = 0

        for i in range(1, n):
            # already in order
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                # if we have to swap on i, we also swap on i - 1 to cancel it out
                swap[i] = swap[i - 1] + 1
                no_swap[i] = no_swap[i - 1]
            # swapping on either i - 1 or i will make A, B increasing
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                swap[i] = min(swap[i], no_swap[i - 1] + 1)  # swap on i
                no_swap[i] = min(no_swap[i], swap[i - 1])  # swap on i + 1
            # otherwise A[i] == B[i]
        return min(swap[-1], no_swap[-1])
# O(n) time and space (can optimize space to O(1))
