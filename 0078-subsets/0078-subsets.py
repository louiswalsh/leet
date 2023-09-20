class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        subset = []

        def dfs(i):
            print("Entering dfs({})".format(i)) 
            if i >= len(nums):
                print(subset)
                result.append(subset[:])  # Append a copy of subset
                print("Exiting dfs({})".format(i)) 
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return result
