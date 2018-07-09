# topological ordering: starting from vertices with no in-edge, to the vertices with no out-edge
# the vertices in the cycle won't be added to queue, which can be used to determine if valid

# Course Schedule
# an in-edge from vertex a to b => a is the prerequisite to b
# determine if one can finish all the courses
# assumption: no duplicate edges
def can_finish(num_courses, prerequisites):
    """
    :type num_courses: courses labeled from 0 to num_courses - 1
    :type prerequisites: array of [post, pre] course pairs
    :rtype: boolean
    """
    graph = { i: set() for i in range(num_courses) }  # course: corresponding post courses
    in_degrees = { i: 0 for i in range(num_courses) }  # course: number of prerequisite courses

    for post_course, pre_course in prerequisites:
        graph[pre_course].add(post_course)
        in_degrees[post_course] += 1

    # vertices that have no in edges
    queue = [i for i in range(num_courses) if in_degrees[i] == 0]
    num_can_finish = 0
    while queue:
        course = queue.pop(0)
        num_can_finish += 1
        for post_course in graph[course]:
            in_degrees[post_course] -= 1
            # each time an in-edge is removed, if a vertex no longer has in-edges,
            # add that vertex to check list
            if in_degrees[post_course] == 0:
                queue.append(post_course)
    # if there's cycle some of the vertices will never get into the queue
    return num_can_finish == num_courses
# O(V+E) time and space


# Alien Dictionary
# There is a new alien language which uses the latin alphabet. However, the order among letters
# are unknown to you. You receive a list of non-empty words from the dictionary, where words
# are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.

# example:
# f(["wrt", "wrf", "er", "ett", "rftt"]) => "wertf"
# f(["z", "x", "z"]) => ""  (invalid order)

# assumptions:
# all letters are in lowercase
# there may be multiple valid order of letters, return any one of them is fine
def alien_order(words):
    """
    :type words: List[str]
    :rtype: str
    """
    # 1. set up graph
    chars = set()
    for word in words:
        for char in word:
            chars.add(char)

    graph = { char: set() for char in chars }  # char: chars after
    in_degrees = { char: 0 for char in chars }  # char: number of chars before it

    # 2. map edges to node => set of nodes
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_length = min(len(w1), len(w2))

        j = 0  # find first different char pair
        while j < min_length and w1[j] == w2[j]:
            j += 1

        if j < min_length:
            if w2[j] not in graph[w1[j]]:  # avoid counting duplicate edges
                in_degrees[w2[j]] += 1
            graph[w1[j]].add(w2[j])

    # 3. start topological sort
    # vertices that have no in edges
    queue = [char for char in chars if in_degrees[char] ==0]
    order = []
    while queue:
        char = queue.pop(0)
        order.append(char)
        for char_next in graph[char]:
            in_degrees[char_next] -= 1
            if in_degrees[char_next] == 0:
                queue.append(char_next)

    return ''.join(order) if len(order) == len(chars) else ''


# Graph Valid Tree
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
# check whether these edges make up a valid tree (note: not necessarily a binary tree!)
# f(5, [[0,1], [0,2], [0,3], [1,4]]) => True
# f(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]) => False
def valid_tree(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """
    if n == 1 and not edges:
        return True
    # 1. set up graph
    graph = { i: set() for i in range(n) }
    in_degrees = { i: 0 for i in range(n) }

    # 2. map edges to node => set of nodes
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)
        in_degrees[i] += 1
        in_degrees[j] += 1

    # 3. start topological sort
    queue = [i for i in range(n) if in_degrees[i] == 1]
    num_valid_nodes = 0
    while queue:
        i = queue.pop(0)
        num_valid_nodes += 1
        for j in graph[i]:
            # key diff below, avoid reducing in-degree twice
            # the node(s) with in-degree 0 will be root(s)
            graph[j].remove(i)
            in_degrees[j] -= 1
            if in_degrees[j] == 1:
                queue.append(j)
    # if there're two or more trees
    if len([d for d in in_degrees.values() if d == 0]) > 1:
        return False
    return num_valid_nodes == n
# thought process: to be a valid tree => all nodes connected but no cycles
