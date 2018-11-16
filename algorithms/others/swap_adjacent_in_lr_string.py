# Swap Adjacent in LR String
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
# a move consists of either replacing one occurrence of "XL" with "LX",
# or replacing one occurrence of "RX" with "XR" (not the other way around).
# assume both strings only contain 'L', 'R', and 'X'.
# Example:
# f("RXXLRXRXL", "XRLXXRRLX") => true
# f("XXXXXLXXXX", "LXXXXXXXXX") => false
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        # observation: 'L' can move left and 'R' can move right
        bal_L = bal_R = 0
        for i in range(len(start)):
            # if this 'L' can move further left, corresponding 'L' in end will appear first
            if start[i] == 'L':
                bal_L -= 1
            if end[i] == 'L':
                bal_L += 1
            # if this 'R' in start can move further right, corresponding 'R' in end will appear later
            if start[i] == 'R':
                bal_R += 1
            if end[i] == 'R':
                bal_R -= 1
            # balance should always non-negative (otherwising missing chars)
            # only one 'L' or 'R' can move at the same time (otherwise will collide)
            if bal_L < 0 or bal_R < 0 or bal_L * bal_R != 0:
                return False

        return bal_L == bal_R == 0
