# assumption: t is not empty
def findAnagrams(self, s, t):
    # s - string, t - target
    # if the balance of char counts are all 0 then
    # a substring is anagram to t
    # => sliding window
    if len(s) < len(t):
        return []
    result = []
    # update the initial balance from t
    balance = {}
    for c in t:
        balance[c] = balance.get(c, 0) + 1

    for i, c in enumerate(s):
        # when a char moves in, update the count
        balance[c] = balance.get(c, 0) - 1
        # when a char moves out of the window, add the count back
        if i >= len(t):
            char_out = s[i - len(t)]
            balance[char_out] += 1
        # check the requirement of the problem
        if all([v == 0 for v in balance.values()]):
            result.append(i - len(t) + 1)
    return result
# since the balance dict contains only a limited set of keys
# the call of all() can be treated as O(1) operation
# thus making it O(n) time and O(1) space