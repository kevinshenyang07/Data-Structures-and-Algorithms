def word_search(board, word):
    if not any(board):
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False

def dfs(board, word, i, j):
    # end condition
    if word == '':
        return True
    # stop conditions
    if i < 0 or i > len(board) or j < 0 or j > len(board[0]) or word[0] != board[i][j]:
        return False
    # mark visited, save as tmp
    tmp = board[i][j]
    board[i][j] = "#"
    # search each direction
    result = False
    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if dfs(board, word[1:], x, y):
            result = True
            break
    # restore the value of the current slot
    board[i][j] = tmp
    return result
