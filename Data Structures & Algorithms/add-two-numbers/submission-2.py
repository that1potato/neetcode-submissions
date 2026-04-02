# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        carry = 0
        out = ListNode(carry)
        head = out
        prev = None
        while n1 and n2:
            s = n1.val + n2.val + out.val
            carry = 1 if s >= 10 else 0
            out.val = s - 10 if carry == 1 else s
            out.next = ListNode(carry)
            prev = out
            n1, n2, out = n1.next, n2.next, out.next
        if n1:
            while n1:
                s = n1.val + out.val
                carry = 1 if s >= 10 else 0
                out.val = s - 10 if carry == 1 else s
                out.next = ListNode(carry)
                prev = out
                n1, out = n1.next, out.next
        else:
            while n2:
                s = n2.val + out.val
                carry = 1 if s >= 10 else 0
                out.val = s - 10 if carry == 1 else s
                out.next = ListNode(carry)
                prev = out
                n2, out = n2.next, out.next
        if out.val == 0:
            prev.next = None
        return head