# Asteroid Collision
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # explode all smaller asteroids going right
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                # special case that both asteroids would explode
                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)

        return stack
