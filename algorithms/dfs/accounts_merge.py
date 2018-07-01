# Accounts Merge

# think Number of Islands
# assumption: if two accounts shares one email, the account name is the same
def accounts_merge(self, accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    def dfs(i, emails):
        # stop condition
        if visited[i]:
            return
        # mark one connected account as visited
        visited[i] = True
        # search each email under one account
        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            emails.add(email)
            for k in mapping[email]:
                dfs(k, emails)

    res = []
    visited = [False] * len(accounts)
    mapping = {}  # email => indices of connected accounts that contains that email

    # generate edges from node (email) to sub-graph (account)
    for i, account in enumerate(accounts):
        for j in range(1, len(account)):
            email = account[j]
            mapping[email] = mapping.get(email, [])
            mapping[email].append(i)

    for i, account in enumerate(accounts):
        if not visited[i]:
            name, emails = account[0], set([])
            # collect emails in connected accounts
            # then mark those accounts as visited
            dfs(i, emails)
            res.append([name] + sorted(emails))

    return res
# O(n) time and space, given n email addresses in total
