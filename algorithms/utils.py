from __future__ import print_function


# reverse string
# strings are immutable in Python, so actually this solution
# takes same space and actually slower than s[::-1],
# since the slicing is optimzed by CPython
def reverse_str(s):
    # convert string to a char array
    chars = list(s)
    # reverse the list in place
    for i in range(len(s) // 2):
        j = len(s) - 1 - i
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)


def is_palindrome(s):
    for i in range(len(s) // 2):
        j = len(s) - 1 - i
        if s[i] != s[j]:
            return False
    return True


if __name__ == '__main__':
    s1 = 'abcdef'
    s2 = 'abba'
    print(reverse_str(s1))
    print(is_palindrome(s1))
    print(is_palindrome(s2))