# Largest Rectangle in Histogram
class Solution(object):
    def largestRectArea(heights):
        heights.append(0)  # ensure the stack is cleared in the end
        stack = [-1]  # increasing stack
        max_area = 0

        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]  # must be max height looking left
                w = i - 1 - stack[-1]  # when look left on (i-1)th bar, the max width that has height h
                max_area = max(max_area, h * w)
            stack.append(i)

        heights.pop()
        return max_area

if __name__ == '__main__':
    largest_rect_area([1, 3, 2, 4, 3, 5])
