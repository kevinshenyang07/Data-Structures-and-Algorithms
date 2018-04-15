def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) <= 2:
        return 0
    vol = 0
    highest = [0] * len(height)
    # max height looking left, both ends cannot contain water
    for i in range(1, len(height) - 1):
        highest[i] = max(highest[i - 1], height[i - 1])
    # update if max height looking right is lower than max height looking left
    for j in range(len(height) - 2, -1, -1):
        highest[j] = min(highest[j], max(highest[j + 1], height[j + 1]))
    # vol trapped on each slot
    for k in range(1, len(height) - 1):
        if highest[k] > height[k]:
            vol += highest[k] - height[k]
    return vol
# O(n) time and space