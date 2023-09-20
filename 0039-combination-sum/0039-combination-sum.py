class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        current = []

        def dfs(i, total):
            if i >= len(candidates) or total > target:
                return

            if total == target:
                result.append(current[:])
                return

            current.append(candidates[i])
            dfs(i, total + candidates[i])
            current.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        print(result)
        return result

            
