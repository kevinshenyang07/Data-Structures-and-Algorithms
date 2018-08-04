# Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    # after sorted, the first and last string has to be the most different ones
    strs.sort()
    first, last = strs[0], strs[-1]
    for i in range(len(first)):
        if i >= len(last) or first[i] != last[i]:
            return first[:i]
    return first
# O(mnlogn) time, where m is the avg string length, n is the number of strings
# usually pretty fast because string comparsion may stop early


# Repeated Substring Pattern
def repeated_substring_pattern(self, s):
    # pattern starting from half length
    for i in range(len(s) // 2, 0, -1):
        # pattern length must be a divisor of the string
        if len(s) % i == 0:
            repititions = len(s) // i
            pattern = s[:i]
            # check if pattern continues
            if pattern * repititions == s:
                return True
    return False


# Longest Palindrome Substring
def longest_palindrome(s):
    max_length = 0
    l = r = 0
    for i in range(len(s) - 1):
        # get palindromes of odd or even length
        l1, r1 = expand_palindrome(s, i, i)
        l2, r2 = expand_palindrome(s, i, i + 1)
        # update longest palindrome
        if r1 - l1 + 1 > max_length:
            max_length = r1 - l1 + 1
            l, r = l1, r1
        if r2 - l2 + 1 > max_length:
            max_length = r2 - l2 + 1
            l, r = l2, r2
    return s[l:r+1]

def expand_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return l + 1, r - 1


# Reverse Words in a String II
def reverse_words(chars):
    # reverse whole string
    reverse(chars, 0, len(chars) - 1)
    # reverse each word
    i, j = 0, 0
    while j < len(chars):
        if j == len(chars) - 1 or chars[j + 1] == ' ':
            reverse(chars, i, j)
            j += 2
            i = j
        else:
            j += 1

def reverse(self, chars, i, j):
    if not chars: return chars

    # deal with index < 0 or > len(chars) - 1
    i = min(i % len(chars), len(chars) - 1)
    j = min(j % len(chars), len(chars) - 1)

    while i < j:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1

    return chars
# O(n) time and O(1) space