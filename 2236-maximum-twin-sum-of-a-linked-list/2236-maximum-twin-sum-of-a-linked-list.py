# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        length = 1
        counter = head

        while counter.next:
            counter = counter.next
            length += 1

        vals = [0] * (length / 2)
        firstHalf = head

        for i in range (length/2) :
            vals[i] += firstHalf.val
            firstHalf = firstHalf.next

        for i in range (length/2 - 1, -1, -1):
            vals[i] += firstHalf.val
            if firstHalf.next:
                firstHalf = firstHalf.next


        return max(vals)