class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        u = sorted(height)
        max_sum = 0
        start = 0
        end = len(height) - 1
        for cur in range(len(u)):
            while start < end and height[start] < u[cur]:
                start = start + 1
            while start < end and height[end] < u[cur]:
                end = end - 1
            max_sum = max(max_sum, (end - start) * u[cur])
        return max_sum