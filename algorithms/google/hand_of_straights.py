# Hand of Straights
# Alice has a hand of cards, given as an array of integers.
# Now she wants to rearrange the cards into groups so that each group is size W,
# and consists of W consecutive cards. Return true if and only if she can.
# hand = [1,2,3,6,2,3,4,7,8], W = 3 => True
# hand = [5,1], W = 2 => False
# Note: consecutive means no nearby cards can be the same number
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        counter = collections.Counter(hand)

        for n in sorted(counter.keys()):
            if counter[n] > 0:
                # should have counter[n] number of straights starting from n
                use_cnt = counter[n]
                for m in range(n, n + W):
                    if counter[m] < use_cnt:
                        return False
                    counter[m] -= use_cnt

        return True
# O(mlogm) time, O(m) space, m being number of distinct cards

# Followup:
# what if W is very large, can we do better than reducing the count card by card?
class SolutionF1(object):
    def isNStraightHand(self, hand, W):
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0

        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1:
                return False

            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W:
                opened -= start.popleft()

        return opened == 0
