class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solutions = []
        base, l, r = 0, 1, 2

        while base < len(nums) - 2:
            l, r = base + 1, len(nums) - 1

            while l < r:
                if nums[base] + nums[l] + nums[r] == 0:
                    if [nums[base], nums[l], nums[r]] not in solutions:
                        solutions.append([nums[base], nums[l], nums[r]])
                    l += 1
                    
                elif nums[base] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

            base += 1

        return solutions