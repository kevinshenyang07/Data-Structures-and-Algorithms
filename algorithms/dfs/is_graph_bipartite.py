# Is Graph Bipartite?
# Note:
# graph will have length in range [1, 100]
# graph[i] will contain integers in range [0, graph.length - 1]
# graph[i] will not contain i or duplicate values
# graph is undirected, and it doesn't contain any element twice
# there is no self edges or parallel edges
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # 0: unknown, -1: left, 1: right
        groups = [0] * len(graph)
        # could be 'island' of nodes, need to search every node
        for i in range(len(graph)):
            # since curr_group is initialized as -1, only search unvisited
            if groups[i] == 0 and not self.dfs(i, graph, -1, groups):
                return False
        return True

    # if node i and its connected nodes can be divided to two groups
    def dfs(self, i, graph, curr_group, groups):
        # stop condition
        if groups[i] != 0:
            return groups[i] == curr_group

        group[i] = curr_group
        for nbr in graph[i]:
            if not self.dfs(nbr, graph, -curr_group, groups):
                return False
        return True
# each node on an edge should belong to different group
# O(N + E) time, N to be number of nodes, E to be number of edges
# traverse each node and all its neighbors once
