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
    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if dfs(board, x, y, word[1:]):
            result = True
            break
    # restore the value of the current slot
    board[i][j] = tmp
    return result
