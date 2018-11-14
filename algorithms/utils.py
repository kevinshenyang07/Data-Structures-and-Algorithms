# prefer list comprehension over map() and filter()
# Python has no switch case, just if / elif

# range of 32-bit signed integer is [- 2 ** 31, 2 ** 31 - 1]
# sys.maxint not the same on diffrent systems, and is deprecated in py3
float('-inf')

3.bit_length() == 2
1 << (x-1).bit_length()  # smallest power of 2 greater than x
bin(num).count('1')  # for a positive integer return number of "1"s in its binary format

copied = [row[:] for row in matrix]  # copy a matrix

# random and collections provided by leetcode by default
# all O(1) time complexity
import random
random.random()
random.randint(start, end)  # inclusive on both ends
random.choice(seq)

#
# interval utils

# two start and end positions
# covers all cases
def overlaps(s1, e1, s2, e2):
    return max(s1, s2) < min(e1, e2)

#
# string utils

# s[i:j] takes O(j - i) time

import string
string.letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.lowercase # a-z
string.digits  # 0-9

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

# test if s is a subseq of t, could be slow if t is large
def naive_is_subsequence(s, t):
    if not s:
        return False
    i = 0  # on s
    for char in t:
        if char == s[i]:
            i += 1
        if i == len(s):
            return True
    return False


#
# linked list utils

# prepend current head to the new list, the current head then becomes new head
def reverse(head):
    new_head = None
    while head:
        curr = head
        head = curr.next
        curr.next = new_head
        new_head = curr
    return new_head

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
    print reverse_str(s1)
    print is_palindrome(s1)
    print is_palindrome(s2)
