# Longest Substring Without Repeating Characters
# the substring has to be continuous
def length_of_longest_substring(s):
    start = max_length = 0
    char_idx = {}  # char: index that char last appeared

    for i in range(len(s)):
        # if there is a repeating char and it's within scope
        if s[i] in char_idx and start <= char_idx[s[i]]:
            # starting from the index after that repeating char
            start = char_idx[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        # update the index anyway
        char_idx[s[i]] = i

    return max_length


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
        if c in balance:
            balance[c] += 1
        else:
            balance[c] = 1

    for i, c in enumerate(s):
        # when a char moves in, update the count
        if c in balance:
            balance[c] -= 1
        else:
            balance[c] = -1
        # when a char moves out of the window, add the count back
        if i >= len(t):
            char_out = s[i - len(t)]
            balance[char_out] += 1
        # check the requirement of the problem
        if all([v == 0 for v in balance.values()]):
            result.append(i - len(t) + 1)
    return result
