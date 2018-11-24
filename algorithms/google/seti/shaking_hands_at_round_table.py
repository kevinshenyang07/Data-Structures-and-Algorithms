# a round table is surrounded by n people, find the ways of people shaking hands
# there're two rules:
# 1. one people can only shake hand with another one people
# 2. two handshakes cannot intersect
#
# example:
# f(4) = 2
#        1        1-2, 3-4
#       ---       1-4, 2-3
#  4  |table| 2   1-3, 2-4 (invalid since line 1-3 intersects with line 2-4)
#       ---
#        3
class HandshakeCounter(object):

    def num_ways(self, n):
        return self.dfs(n, {})  # memo to prevent duplicates to be counted

    def dfs(self, n, memo):
        if n == 0:
            return 1
        if n % 2 == 1:
            return 0
        if n in memo:
            return memo[n]

        count = 0
        # picking person i and any of another person
        # the table is divided into two with sizes of (i - 2) and (n - i)
        for i in range(2, n + 1):
            sub_cnt1 = self.dfs(i - 2, memo)
            sub_cnt2 = self.dfs(n - i, memo)
            count += sub_cnt1 * sub_cnt2
        memo[n] = count
        return count


if __name__ == '__main__':
    counter = HandshakeCounter()
    for n in [4, 6, 8, 10, 12, 14]:
        print "n = {}, count = {}".format(n, counter.num_ways(n))
