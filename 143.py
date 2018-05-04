# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next #divide the list into two half
        
        cur, prev = slow, None
        
        while cur:
            prev, cur.next, cur = cur, prev, cur.next#reverse the second half
        
        while prev.next:                            #merge
            head.next, head = prev, head.next
            prev.next, prev = head, prev.next


    def reorderList2(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        a, cnt, k = [], 0, 0
        dummy = head
        while head:
            cnt += 1
            a.append(head.val)
            head = head.next
    
        a.reverse()
        head = dummy
        while k < cnt // 2:
            new = ListNode(a[k])
            head.next, new.next = new, head.next
            k += 1
            if cnt % 2 or k < cnt // 2:
                head = head.next.next
            else:
                head = head.next
            
        head.next = None
