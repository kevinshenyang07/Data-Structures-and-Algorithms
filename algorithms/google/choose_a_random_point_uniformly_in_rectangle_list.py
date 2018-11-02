import random

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(object):
    # (x1, y1) to be lower-left, (x2, y2) to be upper-right
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.area = (x2 - x1) * (y2 - y1)

class PointPicker(object):
    def select_from_single(self, rect):
        new_x = rect.x1 + random.random() * (rect.x2 - rect.x1)
        new_y = rect.y1 + random.random() * (rect.y2 - rect.y1)
        return Point(new_x, new_y)

    def select_from_multi_non_overlapping(self, rects):
        # raise error if no rects
        n = len(rects)
        total_area = rects[0].area
        acc_areas = [0] * n
        acc_areas[0] = rects[0].area

        for i in range(1, n):
            total_area += rects[i].area
            acc_areas[i] = acc_areas[i - 1] + rects[i].area

        threshold = random.random() * total_area
        for i, acc_area in enumerate(acc_areas):
            if acc_area >= threshold:
                return rects[i]

    def select_from_multi_overlapping(self, rects):
        # firstly do sweep-line on x-axis
        # for each point (x, 0), find rectangles containing that point
        # then do sweep-line on y-axis
        # break those rectangles into smaller ones, and assign proper weights
        pass