from collections import defaultdict, deque

# Closest Leaf in a Binary Tree
# Given a binary tree where every node has a unique value, and a target key k,
# find the value of the nearest leaf node to target k in the tree.
# Here, nearest to a leaf means the least number of edges travelled on the binary tree
# to reach any leaf of the tree. Also, a node is called a leaf if it has no children.
#         1
#        / \
#       2   3
#      /
#     4
#    /
#   5
#  /
# 6
# k = 2 => 3

# approach: turn the tree into graph, then BFS starting from k
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: return -1

        graph, leaves = self.to_graph_and_leaves(root)

        queue = deque([k])
        while queue:
            val = queue.popleft()
            if val in leaves:
                return val
            for nbr in graph[val]:
                queue.append(nbr)
            # to avoid re-visiting neighbors of node has been visited
            graph[val] = []

        return -1

    def to_graph_and_leaves(self, root):
        graph = defaultdict(list)
        leaves = set()
        # need to keep track of leaves since there are cases that root having one child
        # len(graph[n]) does not necessarily mean n is a leaf

        queue = deque([root])
        while queue:
            node = queue.popleft()

            if not node.left and not node.right:
                leaves.add(node.val)

            # add edges to both parent and child nodes
            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

        return graph, leaves

# O(n) time and space

