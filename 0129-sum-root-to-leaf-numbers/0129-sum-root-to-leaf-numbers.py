# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        array = []

        def dfs(root, builtStr):
            builtStr += str(root.val)
            if not root.left and not root.right:
                array.append(builtStr)
                return

            if root.left:
                dfs(root.left, builtStr)

            if root.right:
                dfs(root.right, builtStr)

        dfs(root, '')
        ret = 0
        for n in array:
            print(n)
            ret += int(n)
        return ret
            
