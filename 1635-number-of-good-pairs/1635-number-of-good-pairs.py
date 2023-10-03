class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l, r = 0, 1
        counter = 0

        while l < len(nums) - 1:
            r = l + 1
            while r < len(nums):
                if nums[l] == nums[r] and l < r:
                    counter += 1
                r += 1
            
            l += 1

        return counter
