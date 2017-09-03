# Decode Ways
def num_decodings(s):
    # append possibilities on the right
    # f('1023') = f('102') * f('3')
    #           + f('10') * f('23')
    if s == '':
        return 0
    # res[i] => number of ways for s[:i]
    res = [0 for _ in range(len(s) + 1)]
    res[0] = 1  # cushion
    for i in range(1, len(s) + 1):
        if s[i-1] != '0':
            res[i] += res[i-1]
        if i != 0 and 10 <= int(s[i-2:i]) <= 26:
            res[i] += res[i-2]
    return res[-1]


# the numbers in matrix are non-negative
# the point can only move either down or right
def min_path_sum(matrix):
    # f(i, j) = min(f(i-1, j), f(i, j-1)) + M[i][j]
    pass
