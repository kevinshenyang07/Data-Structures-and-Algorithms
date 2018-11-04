# Give a matrix with m rows and n columns, find the number of ways
# to move from upper left to upper right.
# each time can only move right / upper right / lower right
def num_ways(m, n):
    if m == 0 or n == 0:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for j in range(1, n):
        for i in range(m):
            if i == 0:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j - 1]
            elif i == m - 1:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + dp[i + 1][j - 1]
    return dp[0][n - 1]

# followup1: given three points that each way needs to pass through
# find the new number of ways
def num_ways_v2(m, n, points):
    # ...
    mapping = {}  # col => row
    for r, c in points:
        if c in mapping:
            return 0
        mapping[c] = r
    for j in range(1, n):
        for i in range(m):
            if j in mapping and i != mapping[j]:
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j - 1]
            elif i == m - 1:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + dp[i + 1][j - 1]
    return dp[0][n - 1]

# followup2: return if the points given is possible
def num_ways_v3(m, n, points):
    # just check dp[0][n - 1]
    pass

# followup3: given a height, and each way needs to move down across the height
# find the new number of ways
def num_ways_v4(m, n, height):
    height = min(height, m)
    return num_ways(m, n) - num_ways(height, n)

# followup4: given a heights array, and each way needs to move down across the height in order
def num_ways_v5(m, n, heights):
    # return 0 if heights array is not ascending
    # otherwise it falls back to num_ways_v4
    pass

if __name__ == '__main__':
    print num_ways(4, 4)  # 4
    print num_ways(5, 5)  # 9
    print num_ways(6, 6)  # 21
    print num_ways(6, 3)  # 2
    print num_ways(3, 6)  # 21
