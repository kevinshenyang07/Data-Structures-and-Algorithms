# Snakes and Ladders
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        queue = collections.deque()
        queue.append((1, 0))
        visited = set([1])

        while queue:
            num, steps = queue.popleft()

            if num == n * n:
                return steps

            for next_num in self.next_nums(board, num):
                if next_num not in visited:
                    queue.append((next_num, steps + 1))
                    visited.add(next_num)

        return -1

    def next_nums(self, board, curr_num):
        n = len(board)
        nums = []

        for i in range(1, 7):
            if curr_num + i > n * n:
                continue
            next_num = self.next_num(board, curr_num + i)
            nums.append(next_num)

        return nums

    def next_num(self, board, num):
        n = len(board)

        r = n - 1 - (num - 1) / n
        if (n - r) % 2 == 1:
            c = (num - 1) % n
        else:
            c = n - 1 - (num - 1) % n

        if board[r][c] == -1:
            return num
        return board[r][c]
# O(n ^ 2) time and space, since bfs will at most visited each position once
