class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftIndex, rightIndex = 0, len(numbers) - 1

        while leftIndex < rightIndex:
            if numbers[leftIndex] + numbers[rightIndex] > target:
                rightIndex -= 1
            elif numbers[leftIndex] + numbers[rightIndex] < target:
                leftIndex += 1
            else:
                return [leftIndex + 1, rightIndex + 1]

            