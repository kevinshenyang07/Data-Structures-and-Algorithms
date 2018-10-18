# Trapping Rain Water
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) <= 2:
        return 0

    # highest[i] = min(max(height[:i]), max(height[:i+1]))
    highest = [0] * len(height)

    # both ends cannot contain water
    # find highest bar look left
    for i in range(1, len(height) - 1):
        highest[i] = max(highest[i - 1], height[i - 1])
    # find highest bar look right
    for i in range(len(height) - 2, -1, -1):
        highest_right = max(highest[i + 1], height[i + 1])
        highest[i] = min(highest[i], highest_right)

    vol = 0
    for i in range(1, len(height) - 1):
        if highest[i] > height[i]:
            vol += highest[i] - height[i]  # volume trapped on each slot
    return vol
# O(n) time and space
