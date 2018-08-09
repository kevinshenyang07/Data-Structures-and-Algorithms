# Imagine you have a special keyboard with the following keys:
# Key 1: (A): Print one 'A' on screen.
# Key 2: (Ctrl-A): Select the whole screen.
# Key 3: (Ctrl-C): Copy selection to buffer.
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
# Now, you can only press the keyboard for N times (with the above four keys),
# find out the maximum numbers of 'A' you can print on screen.
# Example:
# f(7) => 9
# (A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V)
class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = range(N + 1)

        for i in range(N + 1):
            for j in range(1, N - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[N]
# O(n ^ 2) time, O(n) space

# thought process:
# 1. All 'A's must be in the beginning of the inputs.
# 2. The 'A's must be followed by a combination of Ctrl-A, Ctrl-C, Ctrl-V.
# 3. Assuming we know the answer of maxA(j), and do Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V...
#    from step j+1 to i, we make (i - j - 1) copies of maxA(j).
#    There must be a j that leads to maxA(i), since it contains all combinations of
#    (Ctrl-A, Ctrl-C) and Ctrl-V, which are derived from sub-problems.
