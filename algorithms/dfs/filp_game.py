# Filp Game II
# Given a string that contains only these two characters: + and -, you and your friend
# take turns to flip two consecutive "++" into "--".
# he game ends when a person can no longer make a move and therefore the other person will be the winner.
# Write a function to determine if the starting player can guarantee a win.
# f('++++) => true
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) < 2:
            return False

        return self.dfs(list(s))

    def dfs(self, state):
        # if any one of moves current player can perform
        # can guarantee the other player won't win, return true
        for i in range(len(state) - 1):
            if state[i] == state[i+1] == '+':
                # search next state
                state[i] = state[i+1] = '-'
                can_other_win = self.dfs(state)
                # roll back to previous state
                state[i] = state[i+1] = '+'

                if not can_other_win:
                    return True

        return False
# improvement: use memo
# O(n!!) time (double factorial)
# first action: at most n - 1 ways to repace '++' to '--,
# second action: at most (n - 2) - 1 ways
# (n/2)th action: (n - 1) * (n - 3) * (n - 5) * ... ~ O(n!!)
