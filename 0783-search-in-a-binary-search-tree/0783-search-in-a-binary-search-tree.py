# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        marker = True
        while marker:
            if val < root.val and root.left:
                root = root.left
            elif val > root.val and root.right:
                root = root.right
            elif val == root.val:
                return root
            else:
                marker = False

        return None

   
        