class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l, r = 0, len(nums) - 1
        index = -1

        while l <= r:
            val = l + (r - l) // 2
            guess = nums[val]

            if guess == target:
                index = val
                break

            elif guess > target:
                r = val - 1
            else: 
                l = val + 1

        
        if index == -1:
            return [-1, -1]

        answer = [index, index]

        i = index
        while i > 0 and nums[i - 1] == target:
            answer[0] -= 1
            i -= 1

        i = index
        while i < len(nums) - 1 and nums[i + 1] == target:
            answer[1] += 1
            i += 1

        return answer