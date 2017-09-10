# Palindrome Partitioning
# 1. seach all possible substrings
# 2. stop early when a substring is not a palindrome
def partition(s):
    def dfs(sub_str, path):
        if not sub_str:
            result.append(path)
            return
        for i in range(1, len(sub_str) + 1):
            if is_palindrome(sub_str[:i]):
                dfs(s[i:], path + [s[:i]])
    result = []
    dfs(s, [])
    return result


def is_palindrome(s):
    # return s == s[::-1]
    for i in range(len(s) // 2):
        j = len(s) - 1 - i
        if s[i] != s[j]:
            return False
    return True
