# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        
        while head:
            if head in stack:
                return True
            else: 
                stack.append(head)
            head = head.next