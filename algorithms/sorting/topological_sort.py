from __future__ import print_function


# Kahn's algorithm - repeatedly remove vertices that have no in edges
# 1. queue up all vertices with no in edges
# 2. Pop off vertices from the queue
#    a. remove vertex and out edges from graph
#    b. push vertex into a sorted array
#    c. examine destination node and push onto queue if no more in edges

# use cases
# 1. task / dependencies (webpack)
# 2. scheduling 


# an in-edge from vertex a to b => a is the prerequisite to b
# determine if one can finish all the courses
def can_finish(num_courses, prerequisites):
    # num_courses: courses labeled from 0 to num_courses - 1
    # prerequisites: array of [post, pre] course pairs
    # return: boolean
    # assumption: no duplicate edges
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
    return num_can_finish == num_courses
# O(V+E) time and O(V+E) space
