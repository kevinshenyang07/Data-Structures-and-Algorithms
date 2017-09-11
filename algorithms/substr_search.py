# Permutation in String
# assumption: input strings only contain lower case letters
def check_inclusion(s1, s2):
    # permutation of s1 in s2 => same counts of different chars
    # in a substring of s2 => sliding window
    if len(s1) > len(s2):
        return False
    # map a-z to 0-25
    A = [ord(char) - ord('a') for char in s1]
    B = [ord(char) - ord('a') for char in s2]
    # count for each letter, will be the diffences of counts
    # between two strings
    balance = [0] * 26
    for x in A:
        balance[x] += 1

    for i, x in enumerate(B):
        # when a char moves in, update the count
        balance[x] -= 1
        if i >= len(A):
            # when a char moves out of the window, add the count back
            balance[B[i - len(A)]] += 1
        if all(b == 0 for b in balance):
            return True
    return False


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
