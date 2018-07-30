# Range Addition
# Assume you have an array of length n initialized with all 0's and are given k update operations.
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments
# each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
# Return the modified array after all k operations were executed.
# Example:
# Given:
# length = 5,
# updates = [
#   [1,  3,  2],
#   [2,  4,  3],
#   [0,  2, -2]
# ]
# => [-2, 0, 3, 5, 3]
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0] * length

        for i, j, val in updates:
            arr[i] += val
            if j < length - 1:
                arr[j+1] -= val

        for i in range(1, length):
            arr[i] += arr[i-1]

        return arr
# approach: only update both ends, cancel out the value accumulated at index j + 1
# [ 0, 0, 0, 0, 0]
# [ 0, 2, 0, 0,-2]
# [ 0, 2, 3, 0,-2]
# [-2, 2, 3, 2,-2]
# => [-2, 0, 3, 5, 3]
