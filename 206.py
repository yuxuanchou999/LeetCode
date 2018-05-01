# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        tmp, curr = ListNode(0), head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        next = None
        while head:
            head.next, next, head = next, head, head.next
        return next    
        
#        if head is None or head.next is None:
#            return head
#        p = self.reverseList(head.next)
#        head.next.next = head
#        head.next = None
#        return  p

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseList(head))
