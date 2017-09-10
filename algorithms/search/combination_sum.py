# notes:
# 1. candidates has no duplicates, each number can be used multiple times
# 2. all numbers in candidates and target are positive integers
# 3. solution does not have duplicate combinations
def combination_sum(candidates, target):
    def dfs(start, path, target):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            # keep adding one number until sum(path) > target
            dfs(i, path + [candidates[i]], target - candidates[i])
    candidates.sort()
    result = []
    dfs(0, [], target)
    return result
