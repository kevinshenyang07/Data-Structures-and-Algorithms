# Is Graph Bipartite?
# Note:
# graph will have length in range [1, 100]
# graph[i] will contain integers in range [0, graph.length - 1]
# graph[i] will not contain i or duplicate values
# graph is undirected
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # 0: unknown, -1: left, 1: right
        group = [0] * len(graph)

        for i, nbrs in enumerate(graph):
            if group[i] == 0 and not self.dfs(i, graph, -1, group):
                return False
        return True

    # if node i and its connected nodes can be divided to two groups
    def dfs(self, i, graph, curr_group, group):
        # stop condition
        if group[i] != 0:
            return group[i] == curr_group

        group[i] = curr_group
        for nbr in graph[i]:
            if not self.dfs(nbr, graph, -curr_group, group):
                return False
        return True
# each node on an edge should belong to different group
# O(N + E) time, N to be number of nodes, E to be number of edges
# traverse each node and all its neighbors once
