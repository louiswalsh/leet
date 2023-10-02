# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        hasSum = [False]

        def dfs(root, runningTotal):
            if not root:
                return

            if runningTotal + root.val == targetSum and not root.left and not root.right:
                hasSum[0] = True
            
            else:
                dfs(root.left, runningTotal + root.val)
                dfs(root.right, runningTotal + root.val)
                

        dfs(root, 0)

        return hasSum[0]