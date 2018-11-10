# Trapping Rain Water
# both ends cannot contain water
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    left = [0] * n  # left[i] =  max(height[:i])
    right = [0] * n  # right[i] = max(height[:i+1])

    # find highest bar looking left
    for i in range(n):
        if i == 0:
            left[i] = height[i]
        else:
            left[i] = max(left[i - 1], height[i])

    # find highest bar looking right
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            right[i] = height[i]
        else:
            right[i] = max(right[i + 1], height[i])

    volume = 0
    for i in range(n):
        volume += min(left[i], right[i]) - height[i]  # volume trapped on each slot
    return volume
# O(n) time and space
