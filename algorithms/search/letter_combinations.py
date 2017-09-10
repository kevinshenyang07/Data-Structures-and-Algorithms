# Letter Combinations of a Phone Number
def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    # mapping from 0 to 9
    mapping = ['', '', 'abc', 'def', 'ghi',
               'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
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
def letter_combinations_rec(digits):
    mapping = ['', '', 'abc', 'def', 'ghi',
               'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    # end cases
    if len(digits) == 0:
        return []
    # since recursion will not produce the correct result
    if len(digits) == 1:
        return list(mapping[int(digits)])
    result = []
    sub_result = letter_combinations_rec(digits[:-1])
    chars = mapping[int(digits[-1])]
    for s in sub_result:
        for c in chars:
            result.append(s + c)
    return result
