def generate_parenthesis(n):
    def dfs(opens, closes, path):
        if opens == n:
            result.append(path + ')' * (n - closes))
            return
        dfs(opens + 1, closes, path + '(')
        if opens > closes:
            dfs(opens, closes + 1, path + ')')

    result = []
    dfs(0, 0, '')
    return result
