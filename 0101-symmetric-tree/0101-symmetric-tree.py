# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isSymmetric = [True]

        def dfs(rootLeft, rootRight):
            if not rootRight and not rootLeft:
                return

            if rootLeft and not rootRight or rootRight and not rootLeft or rootLeft.val != rootRight.val :
                isSymmetric[0] = False
                return


            else:
                dfs(rootLeft.right, rootRight.left)
                dfs(rootLeft.left, rootRight.right)

        dfs(root.left, root.right)
        return isSymmetric[0]
            

            