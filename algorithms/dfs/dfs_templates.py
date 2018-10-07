#
# DFS is enumeration with pruning.
# Three elements (order of 1 and 2 interchangeable):
# 1. valid result condition
# 2. early stop condition
# 3. recursion definition

# DFS method arguments order:
# depth, candidates, sub result, result (by stability)

# combination time complexity: O(2 ^ n)
# => 2 options for each element (although we need to keep track of picked ones)
# permutation time complexity: O(n!)
# => n options picking first element, n - 1 options for second, and so on

def subsets(nums):
    result = [[]]
    for num in sorted(nums):
        # copy the current subsets and add the new element
        result += [item + [num] for item in result]
    return result


def subsets_dfs(nums):
    def dfs(depth, start, path):
        # if nums contain duplicates, check if path in result before append
        result.append(path)
        if depth == len(nums):
            return
        # construct dfs calls by level
        for i in range(start, len(nums)):
            # later numbers get less candidates
            dfs(depth + 1, i + 1, path + [nums[i]])
    nums.sort()  # optional
    result = []
    dfs(0, 0, [])
    return result


def permute(nums):
    perms = [[]]
    # add new element to current permutations on every position
    # [[]] => [[1]] => [[1,2],[2,1]] => ...
    for num in nums:
        new_perms = []
        for perm in perms:
            # insert the number to all possible positions
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [num] + perm[i:])
        perms = new_perms
    return perms


# an approach similar to subsets, add candidates for backtracking
def permute_dfs(nums):
    def dfs(depth, candidates, path):
        if depth == len(nums):
            result.append(path)  # only append full length permutation
            return
        for i in range(len(candidates)):
            # construct dfs calls by level
            # or use candidates.pop(i)
            dfs(depth + 1, candidates[:i] + candidates[i + 1:], path + [candidates[i]])
    nums.sort()  # optional
    result = []
    dfs(0, nums, [])
    return result


# nums can have duplicates, only return unique permutations
def permute_unique(nums):
    def dfs(candidates, path):
        if len(candidates) == 0:
            result.append(path)
            return
        for i in range(len(candidates)):
            # jump to next iteration if the candiate element is the same as previous
            if i > 0 and candidates[i - 1] == candidates[i]:
                continue
            dfs(candidates[:i] + candidates[i + 1:], path + [candidates[i]])
    nums.sort()  # necessary
    result = []
    dfs(0, nums, [])
    return result


if __name__ == '__main__':
    nums = [3, 2, 1]
    print subsets_dfs(nums)
    print permute_dfs(nums)
