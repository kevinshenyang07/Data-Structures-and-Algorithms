# Accounts Merge

# think Number of Islands
def accounts_merge(self, accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    def dfs(i, emails):
        # stop condition
        if visited[i]:
            return
        visited[i] = True
        # search each email under one account
        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            emails.add(email)
            for k in mapping[email]:
                dfs(k, emails)

    visited = [False] * len(accounts)
    mapping = {}
    res = []
    # email => indices of accounts that contains that email
    #          (connected accounts)
    for i, account in enumerate(accounts):
        for j in range(1, len(account)):
            email = account[j]
            mapping[email] = mapping.get(email, [])
            mapping[email].append(i)
    #
    for i, account in enumerate(accounts):
        if visited[i]:
            continue
        name, emails = account[0], set([])
        # collect emails in connected accounts
        # then mark those accounts as visited
        dfs(i, emails)

        res.append([name] + sorted(emails))

    return res
# O(n) time and space, given n email addresses in total
