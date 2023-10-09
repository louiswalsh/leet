class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = -1, -1
        low, high = 0, len(nums) - 1

        # Binary search for the left boundary
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                left = mid
                high = mid - 1  # Continue searching in the left half
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        low, high = 0, len(nums) - 1

        # Binary search for the right boundary
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                right = mid
                low = mid + 1  # Continue searching in the right half
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [left, right]
