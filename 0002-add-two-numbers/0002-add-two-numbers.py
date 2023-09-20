# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []

        while l1:
            list1.append(l1.val)

            if l1.next:
                l1 = l1.next
            else: 
                l1 = None

        while l2:
            list2.append(l2.val)

            if l2.next:
                l2 = l2.next
            else: 
                l2 = None

        list1.reverse()
        list2.reverse()
        str1 = ''
        for n in list1:
            str1 += str(n)

        str2 = ''
        for n in list2:
            str2 += str(n)

        res = int(str1) + int(str2)

        result = None
        prev_node = None

        for i in range(len(str(res)) - 1, -1, -1):
            number = str(res)[i]
            print(number)
            new_node = ListNode(int(number))
            if prev_node:
                prev_node.next = new_node
            else:
                result = new_node
            prev_node = new_node

            
        print(result)
        return result


        