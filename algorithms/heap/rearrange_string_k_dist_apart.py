from heap import Heap

# Rearrange String k Distance Apart
# Given a non-empty string s and an integer k, rearrange the string such that
# the same characters are at least distance k from each other.
# All input strings are given in lowercase letters.
# If it is not possible to rearrange the string, return an empty string "".
# f("aabbcc", 3) => "abcabc"
# f("aaabc", 3) => ""

# similar to Task Schedular
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0: return s

        counter = collections.Counter(s)
        heap = Heap(lambda t: (-t[1], t[0]))
        for char, count in counter.items():
            heap.push((char, count))

        res = []
        while len(res) < len(s):
            curr_group = []  # each group except the last has k chars

            for _ in range(min(k, len(s) - len(res))):
                # no other distinct chars to fill
                if len(heap) == 0:
                    return ''

                char, cnt = heap.pop()
                res.append(char)
                if cnt > 1:
                    curr_group.append((char, cnt - 1))

            for pair in curr_group:
                heap.push(pair)

        return ''.join(res)
# O(nlog(c)) time, O(c) space, given c to be possible types of chars
