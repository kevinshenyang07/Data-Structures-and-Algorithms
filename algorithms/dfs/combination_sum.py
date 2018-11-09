# Combination Sum
# notes:
# 1. candidates have no duplicates, each number can be used multiple times
# 2. all numbers in candidates and target are positive integers
# 3. solution should not have duplicate combinations
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.candidates = candidates
        self.result = []
        self.dfs(target, 0, [])
        return self.result

    def dfs(self, target, start, path):
        if target < 0:
            return
        if target == 0:
            self.result.append(path)
            return
        for i in range(start, len(self.candidates)):
            # keep adding one number until sum(path) > target
            candidate = self.candidates[i]
            self.dfs(target - candidate, i, path + [candidate])


# Combination Sum II
# notes:
# 1. candidates have duplicates, each number can be used only once
# 2. all numbers in candidates and target are positive integers
# 3. solution should not have duplicate combinations
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.candidates = candidates
        self.result = []
        self.dfs(target, 0, [])
        return self.result

    def dfs(self, target, start, path):
        if target < 0:
            return
        if target == 0 and path not in self.result:
            self.result.append(path)
            return
        for i in range(start, len(self.candidates)):
            # skip if the search on previous number has already started
            if i > start and self.candidates[i - 1] == self.candidates[i]:
                continue
            candidate = self.candidates[i]
            self.dfs(target - candidate, i + 1, path + [candidate])
# test case 1:
# [2, 5, 2, 1, 2], 5 => [[1,2,2]]
# test case 2:
# [10,1,2,7,6,1,5], 8 => [[1,2,5],[1,7],[1,1,6],[2,6]]


# Combination Sum III
# Find all possible combinations of k distinct numbers that add up to a number n, given that
# only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# notes:
# 1. all numbers will be positive integers
# 2. the solution set must not contain duplicate combinations
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.k = k
        self.candidates = range(1, 10)
        self.result = []
        self.dfs(n, 0, [])
        return self.result

    def dfs(self, target, start, path):
        if target < 0:
            return
        if target == 0 and len(path) == self.k and path not in self.result:
            self.result.append(path)
            return
        for i in range(start, len(self.candidates)):
            candidate = self.candidates[i]
            self.dfs(target - candidate, i + 1, path + [candidate])
# test case 1:
# k = 3, n = 7 => [[1,2,4]]
# test case 2:
# k = 10, n = 100 => []
