# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        q = collections.deque()
        q.append(root)
        maxSum = -99999999999999999999999999999
        level = 1
        maxLevel = 1

        while q:
            levelSum = 0
            for i in range(len(q)):
                obsNode = q.popleft()
                levelSum += obsNode.val

                if obsNode.left:
                    q.append(obsNode.left)
                if obsNode.right:
                    q.append(obsNode.right)
            print(int(levelSum) > maxSum)
            if int(levelSum) > maxSum:
                print('entered')
                maxLevel = level
                maxSum = levelSum
            level += 1

        return maxLevel
        