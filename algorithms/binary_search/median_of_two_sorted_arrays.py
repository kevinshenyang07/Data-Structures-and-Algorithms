# Median of Two Sorted Arrays
# do it in O(log(m+n)) time
# give this first, then try to optimize
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        total = m + n

        if total % 2 == 1:
            return self.find_kth(A, B, total // 2)
        else:
            return (self.find_kth(A, B, total // 2 - 1) + self.find_kth(A, B, total // 2)) / 2.0

    # zero indexed
    def find_kth(self, A, B, k):
        # avoid j to be out of range in the shorter array
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        # avoid j out of range when len(A) == 1 and k == len(B)
        # k won't be larger than the value below
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])

        # take first i elements in A and first j elements in B
        i = len(A) // 2
        j = k - i

        # no matter how A and B order
        if A[i] > B[j]:
            # all elements in A[i:] > every element in A[:i] + B[:j]
            # => elements in A[i:] have no chance to be in first k elements
            # => to find kth elements in A[:i] and B, at least j elements must come from B
            # => B[:j] must be a subset of first k elements
            # => find (k -j)th element
            return self.findKth(A[:i], B[j:], i)
        else:  # A[i] <= B[j]
            # all elements in B[j:] > every element in A[:i] + B[:j]
            # => elements in B[j:] have no chance to be in first k elements
            # => to find kth element in A and B[:j], at least i elements mush come from A
            # => A[:i] must be a subset of first k elements
            # => find (k - i)th element
            return self.findKth(A[i:], B[:j], j)
