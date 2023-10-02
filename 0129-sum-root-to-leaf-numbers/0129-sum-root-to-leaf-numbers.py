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
        numbers = []

        def dfs(root, currNum):
            if not root:
                return
            
            currNum = str(currNum) + str(root.val)

            if not root.left and not root.right:
                numbers.append(currNum)

            else:
                dfs(root.left, currNum)
                dfs(root.right, currNum)

        
        dfs(root, '')
        result = 0
        
        for n in numbers:
            result += int(n)

        return result


        