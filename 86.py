# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummysmall, dummygreat = ListNode(-1), ListNode(-1)
        small, great = dummysmall, dummygreat
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                great.next = head
                great = great.next
            head = head.next
            
        small.next = dummygreat.next
        great.next = None
        return dummysmall.next
        
        
