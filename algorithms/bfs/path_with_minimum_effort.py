class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row, col = len(heights), len(heights[0])
        efforts = [[float('inf')] * col for _ in range(row)]
        efforts[0][0] = 0

        queue = [(0, 0, 0)]  # LatestEffort, x, y.
        visited = [[False] * col for _ in range(row)]
        while queue:
            # Greedily look for the node with smallest effort, so a node
            # won't be wasted in a suboptimal path.
            # Won't work with negative weights.
            _, x, y= heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                i = x + dx
                j = y + dy
                if 0 <= i < row and 0 <= j < col and not visited[i][j]:
                    # Read the description carefully.
                    localEffort = abs(heights[i][j] - heights[x][y])
                    # Latest effort from (0, 0) to (i, j).
                    effort = max(efforts[x][y], localEffort)
                    if efforts[i][j] > effort:
                        efforts[i][j] = effort
                        heapq.heappush(queue, (effort, i, j))
        return efforts[-1][-1]
