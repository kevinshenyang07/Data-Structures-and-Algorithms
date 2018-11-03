class UnionFind(object):
    '''
    beware that if an element has never been called in .find(),
    its parent might not be the final parent
    '''
    def __init__(self, n):
        self.parents = range(n)
        self.sizes = [1] * n
        self.num_groups = n

    # amortized O(1) time:
    def find(self, p):
        while p != self.parents[p]:
            # path compression
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        # the length of the previous path is now halfed
        return p

    # amortized O(1) time
    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)

        # only union when p and q not in one tree
        # enough for interview, can optimize by merging small to big tree
        if parent_p != parent_q:
            self.parents[parent_q] = parent_p
            self.sizes[parent_p] += self.sizes[parent_q]
            self.num_groups -= 1

# proof of time complexity of #find
# imagine there's only one tree with n nodes, and each node
# only has one child e.g. 0 <- 1 <- ... <- n - 1
# path compression eventually make it a flattened tree
# overall cost is O(n / 2  + n / 4 + n / 8) = O(n)
# divided by n operations => O(1) in average
