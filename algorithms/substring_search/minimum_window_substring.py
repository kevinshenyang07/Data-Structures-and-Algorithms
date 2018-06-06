'''
general approach to substring search problems:
1. have two pointers from the start, keep track of current state
2. move right pointer as far as possible, update global maximum
3. break the criteria by moving the left pointer, then repeat step 2
'''

# assumption1: the answer is guaranteed to be unique
# assumption2: t can have repeating chars

class Solution(object):
    def min_window(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ''
        missing = len(t)
        counter = {}
        for char in t:
            counter[char] = counter.get(char, 0) + 1

        # move right pointer as far as possible to find a valid substring
        # then move left pointer as far as possible to minimize that substring
        i = 0
        for j, char in enumerate(s):
            if char in counter:
                counter[char] -= 1
                if counter[char] >= 0:
                    missing -= 1

            if missing == 0:
                while s[i] not in counter or counter[s[i]] < 0:
                    if s[i] in counter:  # repeating chars
                        counter[s[i]] += 1
                    i += 1

                res_local = s[i:j+1]
                if not res or len(res_local) < len(res):
                    res = res_local
                # start a new search by moving left pointer by one
                missing += 1
                counter[s[i]] += 1
                i += 1

        return res
# O(n) time