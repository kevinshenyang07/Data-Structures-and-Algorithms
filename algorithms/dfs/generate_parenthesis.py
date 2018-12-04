# Generate Parenthesis
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.result = []
        self.dfs("", 0, 0)
        return self.result

    def dfs(self, substr, open_parens, close_parens):
        if open_parens == close_parens == self.n:
            self.result.append(substr)
            return

        if open_parens < self.n:
            self.dfs(substr + "(", open_parens + 1, close_parens)
        if open_parens > close_parens and close_parens < self.n:
            self.dfs(substr + ")", open_parens, close_parens + 1)
