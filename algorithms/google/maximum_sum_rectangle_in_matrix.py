# give an int matrix, find a sub-matrix that maximizes the sum in the area
# prefix sum + maximum continuous subarray
def max_sub_sum(matrix):
    if not any(matrix):
        return 0

    m, n = len(matrix), len(matrix[0])
    pre_sums = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if j == 0:
                pre_sums[i][j] = matrix[i][j]
            else:
                pre_sums[i][j] = pre_sums[i][j - 1] + matrix[i][j]

    res = float('-inf')
    # i, j => column left / right, k => row
    # the sum of each row can be treated as a vertical array
    for j in range(n):
        for i in range(j):
            curr_sum = 0
            for k in range(m):
                if i == 0:
                    sub_sum = pre_sums[k][j]
                else:
                    sub_sum = pre_sums[k][j] - pre_sums[k][i - 1]

                curr_sum = max(curr_sum + sub_sum, sub_sum)
                res = max(res, curr_sum)

    return res

if __name__ == '__main__':
    mat = [
      [1, 2, -1, -4, -20],
      [-8, -3, 4, 2, 1],
      [3, 8, 10, 1, 3],
      [-4, -1, 1, 7, -6 ]
    ]

    print max_sub_sum(mat)
