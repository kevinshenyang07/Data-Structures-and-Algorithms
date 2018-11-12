# All Nodes Distance K in Binary Tree
# return a list of values of all nodes that have a distance K from the target node
# distance between two nodes = length of shortest path
# assume the tree is not empty, all nodes have unique values
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # similar to cloeset leaf in a binary tree,
        # build the graph then do BFS
        graph = self.build_graph(root)

        visited = set([target.val])
        queue = collections.deque([(target.val, 0)])
        res = []

        while queue:
            node_val, dist = queue.popleft()

            if dist == K:
                res.append(node_val)
                continue
            for nbr in graph[node_val]:
                if nbr not in visited:
                    queue.append((nbr, dist + 1))
                    visited.add(nbr)

        return res

    def build_graph(self, root):
        graph = collections.defaultdict(set)

        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
            if node.right:
                queue.append(node.right)
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)

        return graph
