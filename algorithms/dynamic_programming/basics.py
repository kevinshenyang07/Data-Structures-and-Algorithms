# assumption: non-empty string and word list
# O(n^3) time, O(n + w) space
def word_break_n3(s, wordList):
    wordSet = set(wordList)
    dp = [False for i in range(len(s) + 1)]
    dp[0] = True  # cushion

    for i in range(1, len(s) + 1):  # end of slice
        for j in range(i):  # start of slice
            if dp[j] and s[j:i] in wordSet:
                # f(s[:i]) is True
                dp[i] = True

    return dp[-1]


# O(w * n^2) time, O(n) space
def word_break_nw(s, wordList):
    dp = [False for i in range(len(s) + 1)]
    dp[0] = True

    for i in range(1, len(s) + 1):  # end of slice
        for word in wordList:
            j = i - len(word)  # start of slice
            if dp[j] and s[j:i] == word:
                dp[i] = True
    return dp[-1]


# Decode Ways
def num_decodings(s):
    # append possibilities on the right
    # f('1023') = f('102') * f('3')
    #           + f('10') * f('23')
    if s == '':
        return 0
    # res[i] => number of ways for s[:i]
    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = 1  # cushion
    for i in range(1, len(s) + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if i != 0 and 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[-1]


def unique_paths_with_obstacles(grid):
    # f(i, j) = f(i-1, j) + f(i, j-1) if grid[i][j] == 0
    #         = 0 if grid[i][j] == 1
    m, n = len(grid), len(grid[0])
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if grid[i-1][j-1] == 0:
                if i == 1 and j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m][n]


# the numbers in matrix are non-negative
# the point can only move either down or right
def min_path_sum(matrix):
    # f(i, j) = min(f(i-1, j), f(i, j-1)) + M[i][j]
    pass
