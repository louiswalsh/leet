# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        q = collections.deque()
        arr = []

        q.append(root)

        while q:
            val = q.popleft()
            arr.append(val.val)
            if val.left:
                q.append(val.left)
            if val.right:
                q.append(val.right)

        arr.sort()
        return arr[k - 1]


        