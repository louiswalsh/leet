class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        answer = None
        rangeNums = [0, len(nums) - 1]
        

        while rangeNums[0] < rangeNums[1]:
            guess = (rangeNums[0] + rangeNums[1]) // 2
            
            if nums[guess] == target:
                return guess

            elif nums[guess] > target:
                rangeNums[1] = guess - 1
            
            else:
                rangeNums[0] = guess + 1

        if nums[rangeNums[0]] == target:
            return rangeNums[0]
            
        return -1

