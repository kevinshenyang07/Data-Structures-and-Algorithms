from __future__ import print_function
import string

# prefer list comprehension over map() and filter()

string.letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.lowercase # a-z
string.digits  # 0-9

# for 32-bit signed integer (sys.maxint not the same on diffrent systems)
INT_MAX = 2 ** 31 - 1
INT_MIN = - 2 ** 31

bin(num).count('1')  # for a positive integer return number of "1"s in its binary format

# reverse string
# strings are immutable in Python, so this solution takes same space
# and actually is slower than s[::-1], since the slicing is optimzed by CPython
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
