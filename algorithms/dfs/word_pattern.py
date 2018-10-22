# Word Pattern II
class Solution(object):
    def word_pattern_match(self, pattern, word):
        return self.dfs(pattern, word, {})

    def dfs(self, pattern, word, matches):
        # early stop condition
        if len(pattern) == 0 and len(word) > 0:
            return False
        # valid result condition
        if len(pattern) == len(word) == 0:
            return True
        # match pattern[0] from one char to max possible chars
        for i in range(1, len(word) - len(pattern) + 2):
            # pattern[0] is new and not been matched the same way
            if pattern[0] not in matches and word[:i] not in matches.values():
                matches[pattern[0]] = word[:i]
                if self.dfs(pattern[1:], word[i:], matches):
                    return True
                matches.pop(pattern[0])  # this pattern does not work
            # pattern[0] was previously matched in the same way
            elif pattern[0] in matches and matches[pattern[0]] == word[:i]:
                if self.dfs(pattern[1:], word[i:], matches):
                    return True
        return False