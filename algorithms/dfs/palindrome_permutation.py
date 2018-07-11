# Palindrome Permutation II
# Given a string s, return all the palindromic permutations (without duplicates) of it.
# Return an empty list if no palindromic permutation could be form.
# f('aabba') => ['ababa', 'baaab']
class Solution(object):
    def generate_palindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        seed = ''
        for char, count in counter.iteritems():
            if count % 2 == 1:
                if seed: return []
                seed = char
                counter[char] -= 1

        perms = []
        self.dfs(seed, perms, counter)
        return perms

    def dfs(self, perm, perms, counter):
        # valid result condition
        if all([char == 0 for char in counter.values()]):
            perms.append(perm)
            return
        # backtracking
        for char in counter:
            if counter[char] > 0:
                counter[char] -= 2
                self.dfs(char + perm + char, perms, counter)
                counter[char] += 2
# O(((n/2 + 1)!) time, O(n) space