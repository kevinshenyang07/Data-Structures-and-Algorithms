from union_find import UnionFind

# Accpimts Merge
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_id, id_to_name = self.create_mappings(accounts)
        uf = UnionFind(len(email_to_id))

        # union emails within an account
        for account in accounts:
            p = email_to_id[account[1]]
            for i in range(2, len(account)):
                q = email_to_id[account[i]]
                uf.union(p, q)

        # collect emails by tree
        for email, p in email_to_id.iteritems():
            parent = uf.find(p)
            id_to_emails[parent].append(email)

        return [[id_to_name[p]] + sorted(emails) for p, emails in id_to_emails.items()]


    def create_mappings(self, accounts):
        email_to_id = {}
        id_to_name = {}
        idx = 0

        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                if email not in email_to_id:
                    email_to_id[email] = idx
                    id_to_name[idx] = name
                    idx += 1

        return email_to_id, id_to_name
# O(N) time and space, N being total number of emails
