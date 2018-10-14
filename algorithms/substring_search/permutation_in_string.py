from collections import Counter

# Permutaion In String
# fixed-width sliding window
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counter = Counter(s1)

        for i, char in enumerate(s2):
            counter[char] = counter.get(char, 0) - 1
            if i >= len(s1):
                char_left = s2[i - len(s1)]
                counter[char_left] += 1
            if i >= len(s1) - 1 and all([v == 0 for v in counter.values()]):
                return True

        return False