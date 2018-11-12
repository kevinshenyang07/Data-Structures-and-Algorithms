# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


# Clone Graph
# allows duplicate labels / self-cycle
# assumption: it's a connected graph
def clone_graph(node):
    '''
    :type node: UndirectedGraphNode
    :rtype: UndirectedGraphNode
    '''
    if not node:
        return None

    mapping = {}  # original node => copied node
    mapping[node] = UndirectedGraphNode(node.label)
    queue = collections.deque([node])  # original nodes

    while queue:
        curr = queue.popleft()

        for nbr in curr.neighbors:
            # avoid add the same node to queue again in self-cycle
            if nbr not in mapping:
                mapping[nbr] = UndirectedGraphNode(nbr.label)
                queue.append(nbr)
            mapping[curr].neighbors.append(mapping[nbr])
    return mapping[node]


# Search Graph Node
# Given a undirected graph, a node and a target, return the nearest node to
# given node which value of it is target.
# assume there's only one available solution.
def search_node(graph, values, node, target):
    '''
    :type graph: List[UndirectedGraphNode]
    :type values: Dict[UndirectedGraphNode, value]
    :type node: UndirectedGraphNode
    :rtype: UndirectedGraphNode
    '''
    if not graph or not node:
        return None
    if values[node] == target:
        return node
    queue = collections.deque([node])
    visited = set([node])
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if values[neighbor] == target:
                return neighbor
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return None
