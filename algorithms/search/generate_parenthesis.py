def generate_parenthesis(n):
    def dfs(string, open_parens, close_parens):
        # stop on invalid cases
        if open_parens < close_parens:
            return
        # end on full length
        if open_parens == n and close_parens == n:
            result.append(string)
        if open_parens <= n:
            dfs(string + "(", open_parens + 1, close_parens)
        if close_parens <= n:
            dfs(string + ")", open_parens, close_parens + 1)
    result = []
    dfs("", 0, 0)
    return result
