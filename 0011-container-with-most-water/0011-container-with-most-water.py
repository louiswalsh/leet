class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # [1, 3, 6, 2, 3]

        l, r = 0, len(height) - 1
        maxWater = 0

        while l < r:
            maxWater = max((min(height[l], height[r]) * (r - l)), maxWater)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return maxWater

