# Remove Invalid Parentheses
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return ['']

        queue = collections.deque([s])
        visited = set()
        ans = []
        found = False  # minimal removals

        while queue:
            s = queue.popleft()

            if self.is_valid(s):
                ans.append(s)
                found = True
            # do not search for shorter substrings once found minimal removals
            if found:
                continue

            for i in range(len(s)):
                if s[i] not in '()':
                    continue
                new_s = s[:i] + s[i + 1:]
                # add to visited here to avoid appending the same substring
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append(new_s)

        return ans

    def is_valid(self, s):
        bal = 0
        for char in s:
            if char == '(':
                bal += 1
            elif char == ')':
                bal -= 1
            if bal < 0:
                return False
        return bal == 0
# O(2 ^ n) time and space
