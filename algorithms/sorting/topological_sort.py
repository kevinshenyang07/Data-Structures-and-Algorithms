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
    graph = { i: set() for i in range(num_courses) }
    in_degrees = { i: 0 for i in range(num_courses) }
    # for each course, create a prereq list
    # for each course with prereq, add 1 in-degree
    for post, pre in prerequisites:
        graph[post].add(pre)
        in_degrees[post] += 1
    # vertices that have no in edges
    queue = [i for i in range(num_courses) if in_degrees[i] == 0]
    num_can_finish = 0
    while queue:
        vertex = queue.pop(0)
        num_can_finish += 1
        for neighbor in graph[vertex]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)
    return num_can_finish == num_courses
# O(V+E) time and O(V+E) space
