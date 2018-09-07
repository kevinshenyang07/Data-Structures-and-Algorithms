from collections import defaultdict

# Accounts Merge
# think Number of Islands
# assumption: if two accounts shares one email, the account name is the same
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        res = []
        self.visited = [False] * len(accounts)
        self.mapping = defaultdict(list)  # email => indices of connected accounts that contains that email

        # generate edges from node (email) to sub-graph (account)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                self.mapping[email].append(i)

        for i, account in enumerate(accounts):
            if not self.visited[i]:
                name, emails = account[0], set()
                # collect emails in connected accounts, then mark those accounts as visited
                self.dfs(i, emails, accounts)
                res.append([name] + sorted(emails))

        return res

    def dfs(self, i, emails, accounts):
        # stop condition
        if self.visited[i]:
            return
        # mark one connected account as visited
        self.visited[i] = True
        # search each email under one account
        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            emails.add(email)
            for k in self.mapping[email]:
                self.dfs(k, emails, accounts)
# O(n) time and space, given n email addresses in total
