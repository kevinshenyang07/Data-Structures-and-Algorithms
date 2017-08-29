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


# an approach similar to subsets, add candidates for backtracking
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


# nums can have duplicates, only return unique permutations
def permute_unique(nums):
    def dfs(depth, candidates, path):
        if depth == len(nums):
            result.append(path)
            return
        for i in range(len(candidates)):
            # jump to next iteration if the candiate element is the same as previous
            if i !=0 and candidates[i-1] = candidates[i]:
                continue
            dfs(depth + 1, candidates[:i] + candidates[i+1:], path + [candidates[i]])
    nums.sort()  # necessary
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


# modify nums in place, don't return anythin
def next_permutation(nums):
    # 1. find longest decreasing suffix
    # starting from the right side
    start = len(nums) - 1
    while nums[start-1] >= nums[start] and start >= 1:
        start -= 1
    # simply reverse if it's sorted
    if start == 0:
        reverse(nums, 0, len(nums) - 1)
        return
    # 2. with pivot = start - 1, find successor = rightmost index that
    # is greater than pivot value, then swap pivot and successor element
    for i in range(len(nums) - 1, start - 1, -1):
        if nums[start-1] < nums[i]:
            nums[start-1], nums[i] = nums[i], nums[start-1]
            break
    # 3. reverse the suffix
    reverse(nums, start, len(nums) - 1)


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def generate_parenthesis(n):
    def dfs(string, open_parens, close_parens):
        # stop on invalid cases
        if open_parens < close_parens:
            return
        # end on full length
        if open_parens == n and close_parens == n:
            result.append(string)
        if open_parens <= n:
            dfs(string + "(", open_parens + 1, close_parens)
        if close_parens <= n:
            dfs(string + ")", open_parens, close_parens + 1)
    result = []
    dfs("", 0, 0)
    return result


def word_search(board, word):
    if not any(board):
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False


# helper function for word_search()
def dfs(board, i, j, word):
    # end on all chars are found
    if word == '':
        return True
    # stop cases
    if i < 0 or i > len(board) or j < 0 or j > len(board[0]):
        return False
    if board[i][j] != word[0]:
        return False
    # prevent visiting one slot twice
    tmp = board[i][j]
    board[i][j] = "#"
    # search each direction
    result = False
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if dfs(board, x, y, word[1:]):
            result = True
            break
    # restore the value of the current slot
    board[i][j] = tmp
    return result

if __name__ == '__main__':
    nums = [3, 2, 1]
    print(subsets_tmp(nums))
    print(permute(nums))
