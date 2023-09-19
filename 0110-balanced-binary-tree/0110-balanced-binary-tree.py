# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = [True]

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(right - left) > 1:
                result[0] = False
                return 0
                

            return 1 + max(left, right)

        dfs(root)
        return result[0]