from prefix_tree import TrieNode

# Word Search
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.is_match(board, i, j, word, 0):
                    return True
        return False

    # use dfs instead of bfs that visits each cell once, see test case 2
    def is_match(self, board, i, j, word, k):
        if k == len(word) - 1 and board[i][j] == word[k]:
            return True
        if board[i][j] != word[k]:
            return False

        m, n = len(board), len(board[0])

        # backtracking
        char = board[i][j]
        board[i][j] = ''

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and self.is_match(board, x, y, word, k + 1):
                return True

        board[i][j] = char

        return False
# test case 1:
# [["a"]]
# "a"
# => true
# test case 2:
# [["A","B","C","E"],
#  ["S","F","E","S"],
#  ["A","D","E","E"]]
# "ABCESEEEFS"
# => true


# Word Search II
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()

        for word in words:
            curr = root
            for char in word:
                curr.children[char] = curr.children.get(char, TrieNode())
                curr = curr.children[char]
            curr.is_word = True

        self.matched = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, root, '')

        return self.matched

    def dfs(self, i, j, board, node, path):
        char = board[i][j]
        # stop condition
        if char == '#' or char not in node.children:
            return

        path += char
        child = node.children[char]
        # keep searching down after a valid word is found
        if child.is_word:
            self.matched.append(path)
            child.is_word = False  # avoid adding the same word twice

        board[i][j] = '#'  # mark as visited

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                self.dfs(x, y, board, child, path)

        board[i][j] = char  # reset as original value

