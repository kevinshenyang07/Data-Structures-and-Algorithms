# Queue Reconstruction by Height
# after sorting people with height, try to add people with height
# from high to low. since the taller people has already been added,
# the index to insert will be the same as num of people ahead
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
