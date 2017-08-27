from __future__ import print_function


def subsets(nums):
    results = [[]]
    for num in sorted(nums):
        results += [item + [num] for item in results]
    return results


def subsets_dfs(nums):
    def dfs(depth, start, path):
        # if nums contain duplicates, check if path in results
        # before append
        results.append(path)
        if depth == len(nums):
            return
        # construct dfs calls by level
        for i in range(start, len(nums)):
            # later numbers get less options
            dfs(depth + 1, i + 1, path + [nums[i]])
    nums.sort()  # optional
    results = []
    dfs(0, 0, [])
    return results


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
            results.append(path)  # only append full length permutation
            return
        for i in range(len(candidates)):
            # construct dfs calls by level
            dfs(depth + 1, candidates[:i] + candidates[i+1:], path + [candidates[i]])
    nums.sort()  # optional
    results = []
    dfs(0, nums, [])
    return results


def combination_sum():
    pass


if __name__ == '__main__':
    nums = [3, 2, 1]
    print(subsets_dfs(nums))
    print(permute(nums))
