# given a target node in a directed graph, find the shortest cycle including this node
# return the whole path
def shortest_cycle_path(node):
    if not node:  return []

    parents = {}  # visited set / mapping of parents
    queue = collections.deque(node.neighbors)
    while queue:
        u = queue.popleft()
        if u == node:
            break
        for v in u.neighbors:
            if v in parents:
                continue
            parents[v] = u
            queue.append(v)

    if node not in parents:
        return []
    # recover path by parents
    path = []
    curr = node
    while curr:
        path.append(curr)
        curr = parents.get(curr, None)
    path.append(node)
    return path[::-1]
