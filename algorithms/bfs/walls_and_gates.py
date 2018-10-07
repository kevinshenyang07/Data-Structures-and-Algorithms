from collections import deque

# Walls and Gates
class Solution(object):
    def walls_and_gates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not any(rooms): return

        queue = deque()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # each time, increment distnace of surrounding rooms by 1
        # each gate guaranteed to increase radius by 1 (like level order)
        while queue:
            i, j = queue.popleft()
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if self.should_update(rooms, x, y):
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x, y))

    # values can be -1, 0 ~ INF
    def should_update(self, rooms, i, j):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
            return False
        return rooms[i][j] == float('inf')
# O(m * n) time
