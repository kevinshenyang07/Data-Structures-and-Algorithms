# Filp Game II
# Given a string that contains only these two characters: + and -, you and your friend
# take turns to flip two consecutive "++" into "--".
# he game ends when a person can no longer make a move and therefore the other person will be the winner.
# Write a function to determine if the starting player can guarantee a win.
# f('++++) => true
class Solution(object):
    def can_win(self, s):
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
            if state[i] == '+' and state[i+1] == '+':

                state[i] = '-'
                state[i+1] = '-'

                can_next_win = self.dfs(state)

                state[i] = '+'
                state[i+1] = '+'

                if not can_next_win:
                    return True
        # impplies the base case that if no moves can be performed
        # current player can't win
        return False
# follow-up: time complexity
