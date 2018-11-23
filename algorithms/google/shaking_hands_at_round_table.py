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
        state = range(1, n + 1)
        self.memo = {}
        return self.dfs(state)

    def dfs(self, state):
        if not state:
            return 1
        if len(state) % 2 == 1:
            return 0

        key = self.memo_key(state)
        if key in self.memo:
            return self.memo[key]

        count = 0
        for j in range(len(state)):
            for i in range(j):
                if self.memo_key(state[i:j + 1]) in self.memo:
                    continue

                new_state1 = state[i + 1:j]
                new_state2 = state[0:i:-1] + state[j+1:]

                sub_cnt1 = self.dfs(new_state1)
                sub_cnt2 = self.dfs(new_state2)
                count += sub_cnt1 * sub_cnt2

        self.memo[key] = count
        return count

    def memo_key(self, state):
        return hash(tuple(state))


if __name__ == '__main__':
    counter = HandshakeCounter()
    for n in [4, 6, 8, 10]:
        print "n = {}, count = {}".format(n, counter.num_ways(n))
