class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        totalProduct = 0
        leftProduct = [1] * n

        for i in range(1, n):
            leftProduct[i] = (leftProduct[i - 1] * nums[i - 1])

        rightProduct = [1] * n
        for j in range(n - 2, -1, -1):
            rightProduct[j] = rightProduct[j + 1] * nums[j + 1]
        
        outputList = [None] * n

        for k in range(0, n):
            outputList[k] = leftProduct[k] * rightProduct[k]

        # print(leftProduct)
        # print(rightProduct)
        # print(outputList)
        return outputList

        
         