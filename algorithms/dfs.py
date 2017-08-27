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
        for i in range(start, len(nums)):
            dfs(depth + 1, i + 1, path + [nums[i]])
    nums.sort()
    results = []
    dfs(0, 0, [])
    return results


def permutations_rec(nums):
    if len(nums) <= 1:
        return [nums]
    sub_perms = permutations_rec(nums[:-1])
    perms = []
    for sub_perm in sub_perms:
        for i in range(len(sub_perm) + 1):
            perm = sub_perm[:i] + [nums[-1]] + sub_perm[i:]
            perms.append(perm)
    return perms

def combination_sum():

    pass


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(subsets_dfs(nums))
    print(permutations_rec(nums))
