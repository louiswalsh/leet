# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head     
        lenCounter = 1   

        while slow and slow.next:
            slow = slow.next
            lenCounter += 1        

        if (lenCounter == n):
            return head.next

        fast = head

        # Stop at the node before the n'th 
        for node in range(lenCounter - n - 1):
            fast = fast.next

        fast.next = fast.next.next

        return head

        