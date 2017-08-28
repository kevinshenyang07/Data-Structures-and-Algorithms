from __future__ import print_function


def subsets(nums):
    result = [[]]
    for num in sorted(nums):
        result += [item + [num] for item in result]
    return result


def subsets_dfs(nums):
    def dfs(depth, start, path):
        # if nums contain duplicates, check if path in result
        # before append
        result.append(path)
        if depth == len(nums):
            return
        # construct dfs calls by level
        for i in range(start, len(nums)):
            # later numbers get less options
            dfs(depth + 1, i + 1, path + [nums[i]])
    nums.sort()  # optional
    result = []
    dfs(0, 0, [])
    return result


def subsets_tmp(nums):
    if not nums:
        return []
    result = [[]]
    nums.sort()
    subsets_helper(nums, 0, [], result)
    return result


def subsets_helper(nums, start, path, result):
    result.append(path)
    for i in range(start, len(nums)):
        path.append(nums[i])
        subsets_helper(nums, i + 1, path, result)
        path.pop()


def permute(nums):
    perms = [[]]
    # [[]] => [[1]] => [[1,2],[2,1]] => ...
    for num in nums:
        new_perms = []
        for perm in perms:
            # insert the number to all possible positions
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [num] + perm[i:])
        perms = new_perms
    return perms


# an approach similar to subsets
def permute_dfs(nums):
    def dfs(depth, candidates, path):
        if depth == len(nums):
            result.append(path)  # only append full length permutation
            return
        for i in range(len(candidates)):
            # construct dfs calls by level
            dfs(depth + 1, candidates[:i] + candidates[i+1:], path + [candidates[i]])
    nums.sort()  # optional
    result = []
    dfs(0, nums, [])
    return result


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


# Palindrome Partitioning
# 1. seach all possible substrings
# 2. stop early when a substring is not a palindrome
def partition(s):
    def dfs(sub_str, path):
        if not sub_str:
            result.append(path)
            return
        for i in range(1, len(sub_str) + 1):
            if is_palindrome(sub_str[:i]):
                dfs(s[i:], path + [s[:i]])
    result = []
    dfs(s, [])
    return result

def is_palindrome(s):
    # return s == s[::-1]
    for i in range(len(s) // 2):
        j = len(s) - 1 - i
        if s[i] != s[j]:
            return False
    return True


if __name__ == '__main__':
    nums = [3, 2, 1]
    print(subsets_tmp(nums))
    print(permute(nums))
