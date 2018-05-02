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


# idea:
# if s[left:right] has all chars in T, calculate distance and keep answer, then move left pointer.
# if s[left:right] doesn't have all chars in T, move right pointer.
# implmentation:
# 1.if all window from left to right contains all chars in t
#   calculate min window length, and keep answer
#   then move left pointer
# 2.else there are missing string in current answer
#   move right pointer
#   update counter
# repeat 1, 2 steps until right is equal to len(s), then break it
def minWindow(self, s, t):

    if len(s) < len(t):
        return ""

    balance = {}
    for c in t:
        balance[c] = balance.get(c, 0) + 1

    left = right = 0
    min_length = len(s) + 1
    answer = ""

    while right <= len(s):
        # check all chars in t that are in the current answer
        if all([v <= 0 for v in balance.values()]):
            if right - left < min_length:
                min_length = right - left
                answer = s[left:right]
            if s[left] in balance:
                balance[s[left]] += 1
            left += 1
        else:
            if right == len(s):
                break
            if s[right] in balance:
                balance[s[right]] -= 1
            right += 1

    return answer
