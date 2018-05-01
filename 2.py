class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        i = 0
        current, carry1, carry2 = l3, 0, 0
        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if i == 0:
                current.next = ListNode(val)
                i += 1
            elif i == 1:
                carry1, val = divmod(val, 10)
                current.next = ListNode(val)
                i += 1
            else:
                carry2, val = divmod(val, 10)
                current.next = ListNode(val)
            current = current.next

        return l3.next, carry1, carry2


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(9), ListNode(4), ListNode(9)
    b, b.next, b.next.next = ListNode(4), ListNode(6), ListNode(5)
    result, carry1, carry2 = Solution().addTwoNumbers(a, b)
    if (result.next.val + carry2) > 9:
        carry1 += 1
    print("{0} -> {1} -> {2}".format(result.val + carry1, (result.next.val + carry2) % 10, result.next.next.val))
