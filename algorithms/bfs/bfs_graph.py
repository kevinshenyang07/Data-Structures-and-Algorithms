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
    queue = [node]  # original nodes
    while queue:
        curr = queue.pop(0)
        # creating a new node here will cause neighbor not to be added
        # in the queue since it's already in the mapping
        for neighbor in curr.neighbors:
            if neighbor not in mapping:
                mapping[neighbor] = UndirectedGraphNode(neighbor.label)
                queue.append(neighbor)
            # append a copied neighbor
            mapping[curr].neighbors.append(mapping[neighbor])
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
    queue = [node]
    visited = set([node])
    while queue:
        curr = queue.pop(0)
        for neighbor in curr.neighbors:
            if values[neighbor] == target:
                return neighbor
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return None
