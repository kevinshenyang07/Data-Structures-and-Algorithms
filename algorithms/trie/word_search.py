from prefix_tree import TrieNode

# Word Search
class SolutionQ1(object):
    def exist(self, board, word):
        if not any(board):
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        m, n = len(board), len(board[0])
        # end condition
        if word == '':
            return True
        # stop conditions
        if i < 0 or i >= m or j < 0 or j >= n or word[0] != board[i][j]:
            return False
        # mark visited, save as tmp
        tmp = board[i][j]
        board[i][j] = "#"
        # search each direction
        result = False
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if self.dfs(board, x, y, word[1:]):
                result = True
                break
        # restore the value of the current slot
        board[i][j] = tmp
        return result


# Word Search II
class SolutionQ2(object):
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

        found = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, root, '', found)

        return found

    def dfs(self, i, j, board, node, path, found):
        char = board[i][j]

        if char == '#' or char not in node.children:
            return

        # add char after validation
        path += char
        # find a valid word, but keep searching down
        node_next = node.children[char]
        if node_next.is_word:
            found.append(path)
            node_next.is_word = False  # avoid adding the same word twice

        board[i][j] = '#'  # mark as visited

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                    continue
                self.dfs(x, y, board, node_next, path, found)

        board[i][j] = char  # reset as original value

