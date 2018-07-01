# s: catsanddog
# words: ['cat', 'cats', 'and', 'sand', 'dog']
# returns all possible breaks

#
# memoized dfs
def word_break_dfs(s, words):
    return dfs(s, words, {})

def dfs(s, words, memo):
    if s in memo:
        return memo[s]  # cached case

    result = []
    for word in words:
        if word == s:  # end case
            result.append(word)
        elif word == s[:len(word)]:
            sub_result = dfs(s[len(word):], words, memo)
            for sub in sub_result:
                result.append(word + ' ' + sub)

    memo[s] = result
    return result


#
# dp + dfs approach
def word_break_dp(s, words):
    def dfs(i, s, path):
        if i < 0:
            return
        if i == 0:
            result.append(' '.join(path))
            return
        for word in dp[i]:
            if word != s[-len(word):]:
                continue
            dfs(i - len(word), s[:-len(word)], [word] + path)

    dp = getDp(s, words)
    result = []
    dfs(len(s), s, [])
    return result


def getDp(self, s, words):
    dp = [[] for _ in range(len(s) + 1)]
    dp[0] = [True]

    for i in range(1, len(s) + 1):
        for word in words:
            if dp[i-len(word)] and word == s[i-len(word):i]:
                dp[i].append(word)
    return dp