import string
from collections import deque

# Word Ladder
def ladder_length(begin_word, end_word, word_list):
    # all the words after begin_word need to be in word list
    if end_word not in word_list:
        return 0
    length = 2
    left, right = set([begin_word]), set([end_word])
    word_set = set(word_list)
    # two-end BFS
    while left:
        left = get_adj_words(left, word_set)
        if left & right:
            return length
        length += 1
        # swap to generate smaller set
        if len(left) > len(right):
            left, right = right, left
        # avoid cycle
        # only remove the words in the left when the left is determined
        # since left is end of current path
        word_set -= left
    return 0

def get_adj_words(source_words, word_set):
    adj_words = set([])
    for word in source_words:
        for i in range(len(word)):
            for char in string.lowercase:
                candidate_word = word[:i] + char + word[i+1:]
                if candidate_word in word_set:
                    adj_words.add(candidate_word)
    return adj_words


# Surrounded Regions
# only horizontal and vertical are considered as adjacent
def solve(board):
    if not any(board): return  # any() takes care of [] and [[]]
    m, n = len(board), len(board[0])
    # get coordinates on the edge
    coors = [coor for k in range(m+n) for coor in ((0, k), (m-1, k), (k, 0), (k, n-1))]
    while coors:
        i, j = coors.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            # mark 'O's connected to the edge as 'T'
            board[i][j] = 'T'
            # add nearby slots
            coors += [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]
    for row in board:
        for i, c in enumerate(row):
            row[i] = 'O' if c == 'T' else 'X'


# Graph Valid Tree:
# Give n nodes labeled from 0 to n-1, and a list of undirected edges
# check if these edges make up a valid tree
def valid_tree(n, edges):
    '''
    :type n: int
    :type edges: List[[int, int]]
    :rtype: boolean
    '''
    if n == 0:
        return False
    if len(edges) != n - 1:
        return False
    queue = deque([0])
    node_set = set([0])
    while queue:
        curr = queue.popleft()
        for i in range(len(edges)):
            # since edges are undirected, need to check both
            if edges[i][0] == curr and edges[i][1] not in node_set:
                queue.append(edges[i][1])
                node_set.add(edges[i][1])
            if edges[i][1] == curr and edges[i][0] not in node_set:
                queue.append(edges[i][0])
                node_set.add(edges[i][0])
    return len(node_set) == n
