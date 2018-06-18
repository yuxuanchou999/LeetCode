# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        cnt = 1
        cur = head
        while head and head.next:
            cnt += 1
            head = head.next
        end = head
        end.next = cur
        k = cnt - (k % cnt) - 1
        while k > 0:
            cur = cur.next
            k -= 1
        dummy = cur.next
        cur.next = None
        return dummy
            
