import string


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def ladder_length(begin_word, end_word, word_list):
    # all the words after begin_word need to be in word list
    if end_word not in word_list:
        return 0
    length = 2
    left, right = set([begin_word]), set([end_word])
    word_set = set(word_list)
    # two-end BFS, 
    while left:
        left = get_adj_words(left, word_set)
        if left & right:
            return length
        length += 1
        # swap to generate smaller set
        if len(left) > len(right):
            left, right = right, left
        # avoid cycle
        # only remove the words in the left when the left is determined
        # since left is end of current path
        word_set -= left
    return 0


def get_adj_words(source_words, word_set):
    adj_words = set([])
    for word in source_words:
        for i in range(len(word)):
            for char in string.lowercase:
                candidate_word = word[:i] + char + word[i+1:]
                if candidate_word in word_set:
                    adj_words.add(candidate_word)
    return adj_words


def level_order(root):
    if not root:
        return []
    queue = [root]
    visited = []
    while queue:
        level = []
        size = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            level.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        visited.append(level)
    return visited


# each node has a unique label
def clone_graph(node):
    '''
    :type node: UndirectedGraphNode 
    :rtype: UndirectedGraphNode 
    '''
    if not node:
        return None
    node_new = UndirectedGraphNode(node.label)
    queue = [node]  # original nodes
    mapping = {}  # label => new node
    mapping[node.label] = node_new 
    while queue:
        curr = queue.pop(0)
        for neighbor in curr.neighbors:
            if neighbor.label not in mapping:
                mapping[neighbor.label] = UndirectedGraphNode(neighbor.label)
                queue.append(neighbor)
            curr_new = mapping[curr.label]
            curr_new.neighbors.append(mapping[neighbor.label])
    return node_new


def cloneGraph(self, node):
    if not node:
        return node
    root = UndirectedGraphNode(node.label)
    stack = [node]
    visit = {}
    visit[root.label] = root

    while stack:
        top = stack.pop()
        for n in top.neighbors:
            if n.label not in visit:
                stack.append(n)
                visit[n.label] = UndirectedGraphNode(n.label)
            visit[top.label].neighbors.append(visit[n.label])

    return root


# Graph Valid Tree: 
# Give n nodes labeled from 0 to n-1, and a list of undirected edges
# check if these edges make up a valid tree
def valid_tree(n, edges):
    '''
    :type n: int
    :type edges: List[[int, int]] 
    :rtype: boolean
    '''
    if n == 0:
        return False
    if len(edges) != n - 1:
        return False
    queue = [0]
    node_set = set([0])
    while queue:
        curr = queue.pop(0)
        for i in range(len(edges)):
            # since edges are undirected, need to check both
            if edges[i][0] == curr and edges[i][1] not in node_set:
                queue.append(edges[i][1])
                node_set.add(edges[i][1])
            if edges[i][1] == curr and edges[i][0] not in node_set:
                queue.append(edges[i][0])
                node_set.add(edges[i][0])
    return len(node_set) == n


# Search Graph Node
# Given a undirected graph, a node and a target, return the nearest node to 
# given node which value of it is target. 
# Assume there's only one available solution.
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


