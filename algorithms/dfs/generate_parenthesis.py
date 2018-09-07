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

    def dfs(self, string, open_parens, close_parens):
        n = self.n
        # stop on invalid cases
        if open_parens < close_parens:
            return
        # end on full length
        if open_parens == n and close_parens == n:
            self.result.append(string)
            return

        if open_parens <= n:
            self.dfs(string + "(", open_parens + 1, close_parens)
        if close_parens <= n:
            self.dfs(string + ")", open_parens, close_parens + 1)
