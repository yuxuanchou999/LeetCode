# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a, b = '', ''
        while l1:
            a += str(l1.val)
            l1 = l1.next
        while l2:
            b += str(l2.val)
            l2 = l2.next
        v = str(int(a) + int(b))   
        head = ListNode(0)
        dummy = head
        for s in v:
            head.next = ListNode(int(s))
            head = head.next
        
        return dummy.next
        
