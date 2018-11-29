import collections

def shortest_common_seq(subseqs):
    graph = collections.defaultdict(set)
    in_degrees = collections.defaultdict(int)

    for subseq in subseqs:
        for i in range(len(subseq)):
            if i == len(subseq) - 1:
                graph[subseq[i]] = graph.get(subseq[i], set())
            else:
                u, v = subseq[i], subseq[i + 1]
                graph[v].add(u)
                in_degrees[u] += 1

    queue = collections.deque(v for v in graph if in_degrees[v] == 0)
    common_seq = []

    while queue:
        v = queue.popleft()
        common_seq.append(v)

        for nbr in graph[v]:
            in_degrees[nbr] -= 1
            if in_degrees[nbr] == 0:
                queue.append(nbr)

    return common_seq[::-1]


# [[2, 3], [3, 3, 3]] => [2, 3, 3, 3]
# [[4, 3], [3, 3, 3]] => [3, 3, 4, 3]
def shortest_common_seq_with_dup(subseqs):
    pass


if __name__ == '__main__':
    print shortest_common_seq([[1, 9, 7], [1, 4], [4, 9], [2]])  # [1, 4, 9, 7, 2]
