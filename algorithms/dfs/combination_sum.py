# notes:
# 1. candidates has no duplicates, each number can be used multiple times
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

        candidates = self.candidates
        for i in range(start, len(candidates)):
            # keep adding one number until sum(path) > target
            self.dfs(target - candidates[i], i, path + [candidates[i]])
