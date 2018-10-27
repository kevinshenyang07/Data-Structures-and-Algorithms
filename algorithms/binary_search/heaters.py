# Heaters
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        # boundary of radius
        lower, upper = 0, max(houses[-1], heaters[-1]) - houses[0]

        while lower + 1 < upper:
            mid = lower + (upper - lower) / 2
            if self.can_cover(houses, heaters, mid):
                upper = mid
            else:
                lower = mid

        if self.can_cover(houses, heaters, lower):
            return lower
        else:
            return upper

    def can_cover(self, houses, heaters, radius):
        i = 0
        for house in houses:
            # check next if current heater cannot warm current house
            while i < len(heaters) and not (heaters[i] - radius <= house <= heaters[i] + radius):
                i += 1
            if i >= len(heaters):
                return False
        return True
# O(max(mlogm, nlogn)) time, O(1) space
# m being number of houses, n being number of heaters

# test case 1:
# [1,2,3,4]
# [1,4]
# => 1

# test case 2:
# [1,1,1,1,1,1,999,999,999,999]
# [499,500,501]
# => 498
