# Flatten 2D Vector
# Implement an iterator to flatten a 2d vector.
# [[1, 2], [], [3]] => [1, 2, 3]
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        val = self.vec[self.i][self.j]

        if self.j == len(self.vec[self.i]) - 1:
            self.i += 1
            self.j = 0
        else:
            self.j += 1

        return val


    def hasNext(self):
        # skip empty arrays
        while self.i < len(self.vec) and not self.vec[self.i]:
            self.i += 1

        return self.i < len(self.vec):
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
