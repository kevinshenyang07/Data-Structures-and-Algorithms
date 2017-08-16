from __future__ import print_function
from .linked_list import LinkedList

# need to implement own hash function
class HashMap(object):
    def __init__(self, num_buckets=8):
        self.store = [LinkedList()] * num_buckets
        self.count = 0

    # override `in` operator
    def __contains__(self, key):

    def __setitem__(self, key, val):

    def __getitem__(self, key):

    def __delitem__(self, key):

    def __iter__(self):

    def __repr__(self):

    def iteritems():

    def num_buckets():

    def resize(self):

    # return the bucket corresponding to key
    def bucket(key):


hash_map = HashMap()
hash_map["first"] = 1
hash_map["second"] = 2
hash_map["third"] = 3
print("first" in hash_map)  # True
del hash_map["first"]
print(hash_map.count)
# it should call resize() when enough items are inserted
# it should rehash existing values


# whether the letters in a string can be permuted to form a palindrome
def can_string_be_palindrome(string):

print(can_string_be_palindrome("edified"))  # true
print(can_string_be_palindrome("apple"))  # false
print(can_string_be_palindrome("racecar"))  # true
