# give a string S and target string T
# find the minimum length of repeated S that contains T, if not return -1
def repeating_times(S, T):
    if not S or not T: return -1

    min_len = 0
    i = 0
    while i < len(S) and S[i] != T[0]:
        i += 1
    if i == len(S):
        return -1

    for j in range(len(T)):
        if S[i] != T[j]:
            return -1
        i += 1
        if i == len(S):
            min_len += len(S)
            i = 0

    if i < len(S):
        min_len += len(S)

    return min_len

if __name__ == '__main__':
    print repeating_times('', 'abc')  # -1
    print repeating_times('abc', '')  # -1
    print repeating_times('abc', 'bcabcad')  # -1
    print repeating_times('adc', 'bcabcad')  # -1
    print repeating_times('abc', 'ab')  # 3
    print repeating_times('abc', 'bcabcab')  # 9
    print repeating_times('abc', 'abcabcab')  # 9
