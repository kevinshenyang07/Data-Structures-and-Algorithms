from union_find import UnionFind

# Graph Valid Tree
# given n nodes labeled from 0 to n-1 and a list of undirected edges
# write a function to check whether these edges make up a valid tree
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        uf = UnionFind(n)
        # no cycles
        for p, q in edges:
            if uf.find(p) == uf.find(q):
                return False
            uf.union(p, q)
        # no forest
        return uf.num_groups == 1


# DFS
class Solution(object):
    def validTree(self, n, edges):
        graph = { i: set() for i in range(n) }
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        self.graph = graph
        self.visited = set()
        return self.dfs(0) and len(self.visited) == n

    def dfs(self, u):
        # should have no cycle
        if len(self.visited & self.graph[u]) >= 2:
            return False

        self.visited.add(u)

        for v in self.graph[u]:
            if v not in self.visited and not self.dfs(v):
                return False
        return True


# BFS
class Solution(object):
    def validTree(self, n, edges):
        graph = { i: set() for i in range(n) }
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        queue = collections.deque([0])
        visited = set([0])

        while queue:
            u = queue.popleft()
            # should have no cycle
            if len(visited & graph[u]) >= 2:
                return False

            for v in graph[u]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)

        return len(visited) == n
