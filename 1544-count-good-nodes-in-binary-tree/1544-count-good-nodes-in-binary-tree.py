# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        counter = [0]

        def searchNode(root, currentMax):
            if not root:
                return
            
            if root.val >= currentMax:
                counter[0] += 1
                currentMax = root.val
            
            searchNode(root.left, currentMax)
            searchNode(root.right, currentMax)
        
        searchNode(root, root.val)

        return counter[0]


