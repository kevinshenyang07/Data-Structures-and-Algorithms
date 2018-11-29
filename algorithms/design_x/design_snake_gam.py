# Design Snake Game
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.body = collections.deque([(0, 0)])
        self.positions = set([(0, 0)])
        self.food = collections.deque(tuple(f) for f in food)
        self.width, self.height = width, height
        self.deltas = { 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0) }

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return how many pieces of food eaten after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head = self.body[0]
        dx, dy = self.deltas[direction]
        new_head = (head[0] + dx, head[1] + dy)

        # remove the tail first since the new head can be in the previous tail position
        tail = self.body.pop()
        self.positions.remove(tail)

        if not self.valid_move(new_head):
            return -1

        self.body.appendleft(new_head)
        self.positions.add(new_head)
        if self.food and new_head == tuple(self.food[0]):
            self.food.popleft()
            self.body.append(tail)  # add the tail back
            self.positions.add(tail)

        return len(self.positions) - 1

    def valid_move(self, pos):
        x, y = pos
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            return False
        if pos in self.positions:
            return False
        return True
# Your SnakeGame object will be instantiated and called as such:
# snake = SnakeGame(width, height, food)
# res = snake.move(direction)
