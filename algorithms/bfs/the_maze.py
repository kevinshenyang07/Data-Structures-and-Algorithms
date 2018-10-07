from heapq import heappush, heappop


# The Maze
# DFS is easier to get to destination
class SolutionQ1(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        return self.dfs(start[0], start[1], maze, destination)

    def dfs(self, i, j, maze, dest):
        if i == dest[0] and j == dest[1]:
            return True

        maze[i][j] = 2  # mark as visited

        for x, y in self.next_coors(i, j, maze):
            if self.dfs(x, y, maze, dest):
                return True
        return False

    def next_coors(self, i, j, maze):
        m, n = len(maze), len(maze[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        coors = []

        for dx, dy in directions:
            x, y = i + dx, j + dy
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1:
                x += dx
                y += dy
            x -= dx  # take one step back
            y -= dy
            if maze[x][y] == 0:
                coors.append((x, y))

        return coors


# The Maze II
# BFS with priority queue
class SolutionQ2(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        distances = [[float('inf')] * n for _ in range(m)]

        pq = [(0, start[0], start[1])]
        while pq:
            dist, i, j = heappop(pq)
            # elements on destination will be pushed to heap only if elements
            # on prev positions have been popped out
            if [i, j] == destination:
                # when entering this statement, there's only elements on
                # destination in the heap
                return dist
            if distances[i][j] > dist:
                distances[i][j] = dist
                for x, y in self.next_coors(i, j, maze):
                    new_dist = dist + abs(x - i) + abs(y - j)
                    heappush(pq, (new_dist, x, y))

        return -1

    def next_coors(self, i, j, maze):
        m, n = len(maze), len(maze[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        coors = []

        for dx, dy in directions:
            x, y = i + dx, j + dy
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1:
                x += dx
                y += dy
            x -= dx  # take one step back
            y -= dy
            if x != i or y != j:
                coors.append((x, y))

        return coors


# The Maze III
# BFS with prioritiy queue, ball will fall into hole if rolled to that position
class SolutionQ3(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m, n = len(maze), len(maze[0])
        hole = tuple(hole)
        distances = [[float('inf')] * n for _ in range(m)]

        pq = [(0, '', ball[0], ball[1])]
        while pq:
            dist, path, i, j = heappop(pq)
            # see explanation in question II
            if (i, j) == hole:
                return path
            if distances[i][j] > dist:
                distances[i][j] = dist
                for x, y, direction in self.next_coors(maze, i, j, hole):
                    new_dist = dist + abs(x - i) + abs(y - j)
                    new_path = path + direction
                    heappush(pq, (new_dist, new_path, x, y))

        return 'impossible'

    def next_coors(self, maze, i, j, hole):
        directions = {
            'r': (0, 1),
            'l': (0, -1),
            'd': (1, 0),
            'u': (-1, 0)
        }
        m, n = len(maze), len(maze[0])
        coors = []

        for d in directions:
            dx, dy = directions[d]
            x, y = i + dx, j + dy
            # stop if falling into the hole
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1 and (x, y) != hole:
                x += dx
                y += dy
            if (x, y) != hole:
                x -= dx  # take one step back
                y -= dy
            if x != i or y != j:
                coors.append((x, y, d))

        return coors
