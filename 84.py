class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        increase, area, i = [], 0, 0
        while i <= len(heights):
            if not increase or (i < len(heights) and heights[i] > heights[increase[-1]]):
                increase.append(i)
                i += 1
            else:
                last = increase.pop()
                if not increase:
                    area = max(area, heights[last] * i)
                else:
                    area = max(area, heights[last] * (i - increase[-1] - 1))
                    
        return area
