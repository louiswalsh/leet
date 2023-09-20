class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current = []

        def dfs(i):
            if i >= len(nums):
                sorter = current[:]
                sorter.sort()
                if sorter not in result:
                    result.append(sorter)
                return
            
            current.append(nums[i])
            dfs(i + 1)
            current.pop()
            dfs(i + 1)

        dfs(0)
        return result