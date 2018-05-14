def min_distance(word1, word2):
    '''
    definition:

    given word1 and word2, d[i][j] is the edit distance between word1[:i] and word2[:j]

    state trasition function:

    d[i][j] = j                                                   i = 0
            = i                                                   j = 0
            = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1])      xi = yj
            = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + 1)  xi != yj

    d[i-1][j] + 1: insert a char to word1
    d[i][j-1] + 1: delete a char from word2
    d[i-1][j-1]  : distance before adding a char to each string
    '''
    dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    for i in range(len(word1) + 1): dp[i][0] = i
    for j in range(len(word2) + 1): dp[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            cost = 0 if word1[i-1] == word2[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)

    return dp[-1][-1]

