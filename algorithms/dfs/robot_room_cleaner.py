# Robot Room Cleaner
# Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked.
# The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
# When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
# Design an algorithm to clean the entire room using only the 4 given APIs shown below.

# Notes:
# One must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
# The robot's initial position will always be in an accessible cell.
# The initial direction of the robot will be facing up.
# All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
# Assume all four edges of the grid are all surrounded by wall.
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # directions if robot keeps turning right
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.visited = set()
        self.dfs(robot, 0, 0, 0)

    # d: index of current direction
    def dfs(self, robot, x, y, d):

        robot.clean()
        self.visited.add((x, y))

        # for each direction, search down as far as it can and move back along the exact path
        # like drawing the shape of a person's hand
        for _ in range(4):
            dx, dy = self.directions[d]
            next_x, next_y = x + dx, y + dy
            # note that robot.move() will move the robot before the search starts
            if (next_x, next_y) not in self.visited and robot.move():
                self.dfs(robot, next_x, next_y, d)
                # move back from (next_x, next_y) to (x, y)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            # try next direction
            robot.turnRight()
            d = (d + 1) % 4

# Variations:
# 1. what if the layout (grid) is known?
# 2. what if the direction can be passed as an arg to robot.move()
# 3. what if we want to minimize the steps to take?

# Interface:
# class Robot(object):
#     def move(self):
#         """
#         Returns true if the cell in front is open and robot moves into the cell.
#         Returns false if the cell in front is blocked and robot stays in the current cell.
#         :rtype bool
#         """
#
#     def turnLeft(self):
#         """
#         Robot will stay in the same cell after calling turnLeft/turnRight.
#         Each turn will be 90 degrees.
#         :rtype void
#         """
#
#     def turnRight(self):
#         """
#         Robot will stay in the same cell after calling turnLeft/turnRight.
#         Each turn will be 90 degrees.
#         :rtype void
#         """
#
#     def clean(self):
#         """
#         Clean the current cell.
#         :rtype void
#         """
#