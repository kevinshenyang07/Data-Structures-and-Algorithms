# Split Array into Consecutive Subsequences
# You are given an integer array sorted in ascending order (may contain duplicates)
# you need to split them into several subsequences, where each subsequences consist
# of at least 3 consecutive integers. Return whether you can make such a split.
# [1,2,3,3,4,4,5,5] => true
# [1,2,3,4,4,5] => false
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = collections.Counter(nums)
        following = collections.Counter()  # num => number of consecutive subseq that ends at num - 1

        for num in nums:
            # has been used up previously
            if counter[num] == 0:
                continue

            counter[num] -= 1
            # guaranteed to work since nums array is sorted start of each subsequence is known
            if following[num] > 0:
                # append num to one of the subseqs that end at num - 1
                following[num] -= 1
                following[num + 1] += 1
            elif counter[num + 1] > 0 and counter[num + 2] > 0:
                # create a new subseq from num to num + 2
                counter[num + 1] -= 1
                counter[num + 2] -= 1
                following[num + 3] += 1
            else:
                return False

        return True
