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

#
# string utils

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

#
# linked list utils
def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def split(head):
    # assume at least one node
    # zero node situation should be checked before calling
    slow = fast = head
    # while there are at least two more nodes
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None  # avoid cycle
    return head, mid


if __name__ == '__main__':
    s1 = 'abcdef'
    s2 = 'abba'
    print(reverse_str(s1))
    print(is_palindrome(s1))
    print(is_palindrome(s2))
