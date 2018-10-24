import random

# choose a random point uniformly in the list of rectangles
# given a list of rectangles which are not intersect with others, and each rectangle has four points
# write a method to choose a point uniformly for the list of rectangles
# assume the rectangle is parallel to x axis
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(object):
    def __init__(self, x1, y1, x2, y2):
        # x1 < x2, y1 < y2
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.area = (x2 - x1) * (y2 - y1)

    def generate_point(self):
        x = self.x1 + random.randint(0, self.x2 - self.x1)
        y = self.y1 + random.randint(0, self.y2 - self.y1)
        return Point(x, y)

class PointSelector(object):
    def __init__(self, rectangles):
        self.recs = rectangles
        self.total_area = sum(rec.area for rec in rectangles)

    def select(self):
        acc_area = 0

        for rec in self.recs:
            acc_area += rec.area
            if random.randint(0, self.total_area) <= acc_area:
                return rec.generate_point()

# followup: what if the rectangles can be overlapped?
# question: how to calculate probability of overlapped?
