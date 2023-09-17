# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        counter = 1
        counterHead = head
        stack = []

        while counterHead and counterHead.next:
            stack.append(counterHead.val)
            counterHead = counterHead.next
            counter += 1
        
        stack.append(counterHead.val)
        returner = head

        while head and head.next:
            head.val = stack.pop()
            head = head.next
        head.val = stack.pop()

        return returner
        