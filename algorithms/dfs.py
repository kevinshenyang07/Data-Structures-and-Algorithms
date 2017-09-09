from __future__ import print_function


def subsets(nums):
    result = [[]]
    for num in sorted(nums):
        # copy the current subsets and add the new element
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
            if i !=0 and candidates[i-1] == candidates[i]:
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


# Letter Combinations of a Phone Number
def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    # mapping from 0 to 9
    mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    result = [""]
    for digit in digits:
        chars = mapping[int(digit)]
        new_result = []
        for char in chars:
            for sub_str in result:
                new_result.append(sub_str + char)
        result = new_result
    return result


# backtracking version
def letter_combinations_rec(digits):
    mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    # end cases
    if len(digits) == 0:
        return []
    # since recursion will not produce the correct result
    if len(digits) == 1:
        return list(mapping[int(digits)])
    result = []
    sub_result = letter_combinations_rec(digits[:-1])
    chars = mapping[int(digits[-1])]
    for s in sub_result:
        for c in chars:
            result.append(s + c)
    return result


def solve_n_queens(n):
    def dfs(queens, xy_dif, xy_sum):
        p = len(queens)
        # end case
        if p == n:
            solutions.append(queens)
            return
        for q in range(n):
            # continue case
            # when a location (x, y) is occupied, other locations (p, q) where 
            # p + q == x + y or p - q == x - y would be invalid
            if q not in queens and (p - q not in xy_dif) and (p + q not in xy_sum):
                dfs(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
    solutions = []
    dfs([], [], [])
    # convert the result to required format
    result = []
    for solution in solutions:
        board = []
        for i in solution:
            row = "." * i + "Q" + "." * (n - i - 1)
            board.append(row)
        result.append(board)
    return result


# a valid IP address format would be xxx.xxx.xxx.xxx
# where xxx is an integer from 0 to 255
def restore_IP_addresses(s):
    '''
    :type s: str, e.g. '19216801'
    :rtype: List[str], all valid IP addresses
    '''
    def dfs(depth, sub_str, path):
        # stop when too many chars are left
        if len(sub_str) > (4 - depth) * 3:
            return
        # end case
        if depth == 4:
            result.append(path)
            return
        # limit iteration range
        max_length = min(3, len(sub_str))
        for i in range(max_length):
            partial = sub_str[:i+1]
            if int(partial) > 255:
                continue
            # if partial has two digits but starts with 0
            if i > 0 and sub_str[0] == '0':
                continue
            dfs(depth + 1, sub_str[i+1:], path + [partial])

    result = []
    dfs(0, s, [])
    return ['.'.join(r) for r in result]



if __name__ == '__main__':
    nums = [3, 2, 1]
    print(subsets_tmp(nums))
    print(permute(nums))
