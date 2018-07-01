# Walls and Gates
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not any(rooms): return

        queue = []

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # each time, increment distnace of surrounding rooms by 1
        # each gate guaranteed to increase radius by 1 (like level order)
        while queue:
            i, j = queue.pop(0)

            if self.should_update(rooms, i - 1, j):
                rooms[i-1][j] = rooms[i][j] + 1
                queue.append((i - 1, j))

            if self.should_update(rooms, i, j - 1):
                rooms[i][j-1] = rooms[i][j] + 1
                queue.append((i, j - 1))

            if self.should_update(rooms, i + 1, j):
                rooms[i+1][j] = rooms[i][j] + 1
                queue.append((i + 1, j))

            if self.should_update(rooms, i, j + 1):
                rooms[i][j+1] = rooms[i][j] + 1
                queue.append((i, j + 1))

    # values can be -1, 0 ~ INF
    def should_update(self, rooms, i, j):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
            return False
        return rooms[i][j] == 2 ** 31 - 1
# O(m * n) time
