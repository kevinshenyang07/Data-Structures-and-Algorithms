# give a matrix of 0s and 1s, with each row sorted
# find the row with maximum number of zeros
# improvement 1: binary search on each row
#                => O(mlogn)
# improvement 2: find the rightmost zero in the first row, then move down or move right
#                => O(m + n)
def row_with_most_zeros(mat):
    if not any(mat):
        return -1

    m, n = len(mat), len(mat[0])
    row_id = 0
    i = j = 0

    while i < m:
        if mat[i][j] == 0:
            while j < n and mat[i][j] == 0:
                j += 1
            row_id = i
        i += 1

    return row_id

if __name__ == '__main__':
    mat = [[1,1,1], [0,0,1], [0,1,1]]
    print row_with_most_zeros(mat)
