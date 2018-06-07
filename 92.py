class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m - 1):
            pre = pre.next
            
        first = pre.next
        cur = first.next
        for i in range(n - m):
            first.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = first.next
        
        return dummy.next
