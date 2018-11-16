# Longest Increasing Subsequence
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tails[i] = the smallest tail of all increasing subseq with length i+1
        # for example give [4, 5, 6, 3],
        # tails[1] = 5 (from [4, 5], [5, 6])
        tails = [0] * len(nums)
        size = 0

        for num in nums:
            i, j = 0, size
            # find the smallest tail for tails[i]
            while i < j:
                m = (i + j) / 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            size = max(size, i + 1)

        return size


if __name__ == '__main__':
    seq = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    print Solution().lengthOfLIS(seq)
