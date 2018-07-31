from heapq import heappush, heappop


# Rearrange String k Distance Apart
# Given a non-empty string s and an integer k, rearrange the string such that
# the same characters are at least distance k from each other.
# All input strings are given in lowercase letters.
# If it is not possible to rearrange the string, return an empty string "".
# f("aabbcc", 3) => "abcabc"
# f("aaabc", 3) => ""
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0: return s

        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        heap = []
        for char, count in counter.iteritems():
            heappush(heap, (-count, char))

        res = []
        while len(res) < len(s):
            group = []
            for _ in range(min(len(s) - len(res), k)):
                if not heap:
                    return ''
                neg_count, char = heappop(heap)
                res.append(char)
                if neg_count < -1:
                    group.append((neg_count + 1, char))

            for pair in group:
                heappush(heap, pair)

        return ''.join(res)
# O(nlog(c)) time, O(c) space, given c to be possible types of chars
