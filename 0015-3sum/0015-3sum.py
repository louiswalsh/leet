class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        base, left, right = 0, 1, len(nums) - 1
        solutions = []

        while base < len(nums):
            
            while left < right:
                if nums[base] + nums[left] + nums[right] == 0:
                    val = [nums[base], nums[left], nums[right]]
                    val.sort()
                    if val not in solutions:
                        solutions.append(val)
                    right -= 1
                    left += 1

                elif nums[base] + nums[left] + nums[right] < 0:
                    left += 1

                else: 
                    right -= 1

            base += 1
            left = base + 1
            right = len(nums) - 1

        return solutions

