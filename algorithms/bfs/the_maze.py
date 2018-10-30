from heapq import heappush, heappop

# The Maze
# DFS is faster to get to destination
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        visited = set()
        return self.dfs(maze, tuple(start), tuple(destination), visited)

    def dfs(self, maze, curr, dest, visited):
        # early stop condition
        if curr in visited:
            return False
        # valid result condition
        if curr == dest:
            return True

        visited.add(curr)
        # recursion definition
        for coor in self.next_coors(curr[0], curr[1], maze):
            if self.dfs(maze, coor, dest, visited):
                return True

        return False

    def next_coors(self, i, j, maze):
        m, n = len(maze), len(maze[0])
        coors = []

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x, y = i, j
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
            if not (i == x and j == y):
                coors.append((x, y))

        return coors


# The Maze II
# BFS with priority queue is faster in this case
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        visited = set()
        pq = [(0, start[0], start[1])]

        while pq:
            # means every coordinate starts the search with shortest distance
            # and the same coordinate with longer distance will be deduplicated
            # thus overall forming a shortest path
            dist, i, j = heappop(pq)

            if (i, j) in visited:
                continue
            if [i, j] == destination:
                return dist

            visited.add((i, j))

            for coor in self.next_coors(i, j, maze):
                new_dist = dist + abs(coor[0] - i) + abs(coor[1] - j)
                heappush(pq, (new_dist, coor[0], coor[1]))

        return -1

    # same as Q1
    def next_coors(self, i, j, maze):
        m, n = len(maze), len(maze[0])
        coors = []

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x, y = i, j
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
            if not (i == x and j == y):
                coors.append((x, y))

        return coors


# The Maze III
# BFS with prioritiy queue, ball will fall into hole if rolled to that position
# similar approach as Q2
class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m, n = len(maze), len(maze[0])
        visited = set()
        pq = [(0, '', ball[0], ball[1])]

        while pq:
            dist, path, i, j = heappop(pq)

            if (i, j) in visited:
                continue
            if [i, j] == hole:
                return path

            visited.add((i, j))

            for x, y, direction in self.next_coors(maze, i, j, hole):
                new_dist = dist + abs(x - i) + abs(y - j)
                new_path = path + direction
                heappush(pq, (new_dist, new_path, x, y))

        return 'impossible'

    def next_coors(self, maze, i, j, hole):
        m, n = len(maze), len(maze[0])
        directions = {
            'r': (0, 1),
            'l': (0, -1),
            'd': (1, 0),
            'u': (-1, 0)
        }
        coors = []

        for d in directions:
            dx, dy = directions[d]
            x, y = i, j
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
                # stop when reaching the hole
                if [x, y] == hole:
                    break
            if not (x == i and y == j)
                coors.append((x, y, d))

        return coors
