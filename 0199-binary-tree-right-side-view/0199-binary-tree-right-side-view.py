# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        vals = []

        while q:
            vals.append(q[len(q) - 1].val)

            for i in range(len(q)):
                observingNode = q.popleft()

                if observingNode.left:
                    q.append(observingNode.left)

                if observingNode.right:
                    q.append(observingNode.right)

        return vals