# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        result = [True]

        def checkTree(p, q):
            if not p and not q:
                return

            if (p and not q) or (q and not p):
                result[0] = False
                return
            
            if p and q and p.val != q.val:
                result[0] = False
                return
            
            
            checkTree(p.left, q.left)
            checkTree(p.right, q.right)

            
        checkTree(p, q)

        return result[0]
        
