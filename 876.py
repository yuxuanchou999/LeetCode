# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cnt, node = 1, head
        while head.next:
            cnt += 1
            head = head.next
        
        cnt //= 2
        while cnt > 0:
            cnt -= 1
            node = node.next
            
        return node
            
