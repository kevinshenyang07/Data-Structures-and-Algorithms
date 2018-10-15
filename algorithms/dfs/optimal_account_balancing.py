# Optimal Account Balancing
# given a list of transactions between a group of people, with each transaction
# as a tuple (x, y, z), meaining person x send person y amount z of money
# assume x != y and z > 0, id x and y might not be linear
# return the minimum number of transactions required to settle the debt
# Optimal Account Balancing
# given a list of transactions between a group of people, with each transaction
# as a tuple (x, y, z), meaining person x send person y amount z of money
# assume x != y and z > 0, id x and y might not be linear
# return the minimum number of transactions required to settle the debt
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        acc = {}
        for p1, p2, amount in transactions:
            acc[p1] = acc.get(p1, 0) - amount
            acc[p2] = acc.get(p2, 0) + amount
        # cancel out balance pairs with equal amount but different sign
        # then filter out zero balances
        bal = acc.values()
        trans = 0
        for i in range(len(bal)):
            for j in range(i):
                if bal[i] * bal[j] != 0 and bal[i] + bal[j] == 0:
                    bal[i] = bal[j] = 0
                    trans += 1
                    break
        bal = [b for b in bal if b != 0]

        return self.dfs(bal, 0, trans)

    # min number of transactions to settle starting from bal[i]
    # trans: transactions made so far
    def dfs(self, bal, i, trans):
        n = len(bal)
        # find the next balance that needs to be settled
        while i < n and bal[i] == 0:
            i += 1
        # end condition
        if i >= len(bal):
            return trans

        res = float('inf')
        for j in range(i + 1, n):
            if bal[i] * bal[j] < 0:  # different sign
                # a transaction that sets balance at i to 0 (settled)
                # and balance at j to bal[j] + bal[i]
                # values before bal[i + 1] are virtually 0 and then added back
                bal[j] += bal[i]
                res = min(res, self.dfs(bal, i + 1, trans + 1))
                # rollback
                bal[j] -= bal[i]
        return res
