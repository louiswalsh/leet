class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, highestLowerNumber, smallestBiggerNumber):
            if not root:
                return True

            if (root.left and (root.left.val >= root.val or root.left.val <= highestLowerNumber)) or \
               (root.right and (root.right.val <= root.val or root.right.val >= smallestBiggerNumber)):
                return False

            return dfs(root.left, highestLowerNumber, root.val) and dfs(root.right, root.val, smallestBiggerNumber)

        return dfs(root, float('-inf'), float('inf'))
