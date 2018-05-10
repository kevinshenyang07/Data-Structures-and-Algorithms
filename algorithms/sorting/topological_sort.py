# topological ordering: starting from vertices with no in-edge, to the vertices with no out-edge
# cannot have cycles

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
    in_degrees = { i: 0 for i in range(num_courses) }  # course: in-degree
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
