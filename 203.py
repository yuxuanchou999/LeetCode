# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = ListNode(-1)
        dummy = cur 
        while head:
            if head.val != val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None    
        return dummy.next
                
