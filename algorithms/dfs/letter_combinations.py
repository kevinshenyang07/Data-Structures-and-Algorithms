# Letter Combinations of a Phone Number
def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    # mapping from 0 to 9
    mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    result = [""]
    for digit in digits:
        chars = mapping[int(digit)]
        new_result = []
        for char in chars:
            for sub_str in result:
                new_result.append(sub_str + char)
        result = new_result
    return result


# backtracking version
def letter_combinations_backtracking(digits):
    def dfs(s, path):
        if s == '':
            result.append(path)
            return
        for char in mapping[int(s[0])]:
            dfs(s[1:], path + [char])

    if not digits:
        return []
    mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    result = []
    dfs(digits, [])
    return [''.join(chars) for chars in result]
