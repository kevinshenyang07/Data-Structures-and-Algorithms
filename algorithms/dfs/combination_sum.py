# notes:
# 1. candidates has no duplicates, each number can be used multiple times
# 2. all numbers in candidates and target are positive integers
# 3. solution should not have duplicate combinations
def combination_sum(candidates, target):
    def dfs(target, start, path):
        print target, start, path
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            # keep adding one number until sum(path) > target
            dfs(target - candidates[i], i, path + [candidates[i]])
    candidates.sort()
    result = []
    dfs(target, 0, [])
    return result


if __name__ == '__main__':
    candidates = [2, 3, 5]
    combs = combination_sum(candidates, 8)