def max_submatrix(matrix):
    if not any(matrix):
        return [[]]

    m, n = len(matrix), len(matrix[0])
    pre_sum = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if j == 0:
                pre_sum[i][j] = matrix[i][0]
            else:
                pre_sum[i][j] = pre_sum[i][j - 1] + matrix[i][j]

    max_sum = float('-inf')
    # since the sum from column j to column k is pre-computed
    # treat each subrow as a number and do 1D max subarray vertically
    for k in range(n):
        for j in range(k + 1):
            curr_sum = 0
            for i in range(m):
                if j == 0:
                    num = pre_sum[i][k]
                else:
                    num = pre_sum[i][k] - pre_sum[i][j - 1]
                curr_sum = max(curr_sum + num, num)
                max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == '__main__':
    mat = [
      [1, 2, -1, -4, -20],
      [-8, -3, 4, 2, 1],
      [3, 8, 10, 1, 3],
      [-4, -1, 1, 7, -6]
    ]

    print max_submatrix(mat)


