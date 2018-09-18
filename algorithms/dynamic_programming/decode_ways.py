# Decode Ways
# f(01) => 0, f(100) => 0
def num_decodings(s):
    #dp[i] = 0 if s[i-1] == "0"
    #      + dp[i-1] if s[i-1] != "0"
    #      + dp[i-2] if "09" < s[i-2:i] < "27"
    if not s or s[0] == '0': return 0

    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(s)+1):
        if s[i-1] != "0":
            dp[i] += dp[i-1]
        if s[i-2] != "0" and int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]

    return dp[-1]
# dp can be optimized to two variables
