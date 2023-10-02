# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = collections.deque()
        resStack = []

        if root:
            q.append(root)

        while q:
            levelSum = 0
            counter = 0

            for n in range(len(q)):
                counter += 1
                val = q.popleft()
                levelSum += val.val + 0.00000

                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)

            resStack.append(levelSum / counter)


        return resStack

                


        