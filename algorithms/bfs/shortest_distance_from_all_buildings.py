from collections import deque

# Shortest Distance from All Buildings
# 0: empty land, 1: building, 2: obstacle
# can only move four directions

# things to check:
# 1. all buildings need be connected
# 2. a candidate location must be connected to all buildings
# 3. if there is a valid location at all

class Solution(object):
    def shortest_distance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not any(grid): return -1

        m, n = len(grid), len(grid[0])
        # accmulative distance to buildings from a location
        distances = [[0 for _ in range(n)] for _ in range(m)]
        # number of buildings that already updated its distance on a location
        updated_times = [[0 for _ in range(n)] for _ in range(m)]

        buildings = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append((i, j))

        for i, j in buildings:
            connected = self.bfs(i, j, grid, distances, updated_times)
            if connected != len(buildings) - 1:
                return -1

        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if 0 < distances[i][j] < min_dist and updated_times[i][j] == len(buildings):
                    min_dist = distances[i][j]

        return min_dist if min_dist < float('inf') else -1

    def bfs(self, i, j, grid, distances, updated_times):
        queue = deque([(i, j, 0)])
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        visited[i][j] = True
        connected = 0  # number of other buildings connected

        while queue:
            i, j, dist = queue.popleft()
            # four directions
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if self.can_visit(x, y, grid) and not visited[x][y]:
                    if grid[x][y] == 1:
                        connected += 1
                    elif grid[x][y] == 0:
                        distances[x][y] += dist + 1
                        updated_times[x][y] += 1
                        queue.append((x, y, dist + 1))
                    # elif grid[i][j] == 2: pass
                    visited[x][y] = True

        return connected

    def can_visit(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False
        return True
