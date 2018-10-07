# Longest Common Subsequence
def lcs(lhs, rhs):
    '''
    state transition function:

    (i >= 1, j >= 1)
    c[i][j] = c[i-1][j-1] + 1            if x[i] = y[j]
            = max(c[i-1][j], c[i-1][j])  if x[i] != y[j]
    c is a matrix, x and y are inputs
    '''
    l_len = len(lhs)
    r_len = len(rhs)
    c = [[0 for j in range(r_len + 1)] for i in range(l_len + 1)]
    for i in range(l_len):
        for j in range(r_len):
            if lhs[i] == rhs[j]:
                c[i + 1][j + 1] = c[i][j] + 1
            else:
                c[i + 1][j + 1] = max(c[i][j + 1], c[i + 1][j])
    return c


# step 4
def get_lcs(lhs, rhs):
    c = lcs(lhs, rhs)
    print(c)
    i = len(lhs) - 1
    j = len(rhs) - 1
    rst = []
    while j >= 0 and i >= 0:
        # move upper left
        if c[i + 1][j + 1] != c[i][j + 1] and c[i + 1][j + 1] != c[i + 1][j]:
            rst.insert(0, lhs[i])
            # print(i, j)
            i -= 1
            j -= 1
        # move up
        elif c[i + 1][j + 1] == c[i][j + 1]:
            i -= 1
        # move left
        else:
            j -= 1
    return rst


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    res = get_lcs(x, y)
    print res
