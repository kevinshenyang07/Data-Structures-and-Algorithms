# Degree of An Array
def findShortestSubArray(self, nums):
    res = max_degree = 0
    starting_indices = {}
    counter = {}

    for i, num in enumerate(nums):
        starting_indices[num] = starting_indices.get(num, i)
        counter[num] = counter.get(num, 0) + 1

        # first occurence of a num with new max degree
        if counter[num] > max_degree:
            max_degree = counter[num]
            res = i - starting_indices[num] + 1
        # a num has previously reached max degree
        elif counter[num] == max_degree:
            res = min(res, i - starting_indices[num] + 1)

    return res
# O(n) time, O(m) space, m is the number of distinct numbers
