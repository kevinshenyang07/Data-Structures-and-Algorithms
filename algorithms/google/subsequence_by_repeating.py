
import path

# given two strings S and T, determine if S can be a subsequence of n copies of T
def subsequence_by_repeating(S, T):
    if not S: return 0
    if not T: return -1

    i = j = 0  # j to be count of chars used in T
    while i < len(S):
        if S[i] not in T:
            return -1
        while S[i] != T[j % len(T)]:
            j += 1
        # compare next pair of chars
        i += 1
        j += 1

    return int(math.ceil(float(j) / T))

def test():
    print subsequence_by_repeating("", "a")  # 0
    print subsequence_by_repeating("a", "")  # -1
    print subsequence_by_repeating("SDSD", "ADS")  # 3
    print subsequence_by_repeating("SDS", "ADS")  # 2
    print subsequence_by_repeating("SDT", "ADS")  # -1
    print subsequence_by_repeating("aaaaaaaaaa", "xxxxxxaxxxxxxx")  # 10
    print subsequence_by_repeating("aaaaaaaaaa", "axxxxxaxxxxxxx")  # 5

if __name__ == '__main__':
    test()


