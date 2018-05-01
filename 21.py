# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prevhead = ListNode(-1)
        prev = prevhead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                prev = prev.next
                l1 = l1.next
            else:
                prev.next = l2
                prev = prev.next
                l2 = l2.next
        prev.next = l1 if l1 else l2
        return prevhead.next
