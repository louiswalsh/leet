class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maximumWater = 0

        if len(height) == 2:
            return min(height[0], height[1])

        leftIndex, rightIndex = 0, len(height) - 1

        while leftIndex < rightIndex:
            water = min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex)

            maximumWater = max(maximumWater, water)

            if height[leftIndex] < height[rightIndex]:
                leftIndex += 1
            else: 
                rightIndex -= 1

        return maximumWater
        
