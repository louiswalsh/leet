"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root

        q = collections.deque()
        q.append(root)
        temp = []

        while q:

            for _ in range(len(q)):
                obs = q.popleft()

                if len(q) > 0:
                    obs.next = q[0]
                else:
                    obs.next = None

                if obs.left:
                    temp.append(obs.left)
                if obs.right:
                    temp.append(obs.right)

            q += temp
            temp = []

        return root
        