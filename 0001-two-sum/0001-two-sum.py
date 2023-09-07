class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        leftIndex, rightIndex = 0, 1

        while leftIndex < len(nums) - 1:
            while rightIndex < len(nums):
                if nums[rightIndex] + nums[leftIndex] == target:
                    return [leftIndex, rightIndex]
                rightIndex += 1
            
            leftIndex += 1
            rightIndex = leftIndex + 1