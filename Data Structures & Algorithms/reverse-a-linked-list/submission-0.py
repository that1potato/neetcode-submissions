# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        if i is None:
            return
        if head.next is not None:
            j = i.next 
        else:
            return i 
        k = head.next.next if head.next.next is not None else None

        if k is None:
            i.next = None
            j.next = i
            return j
        
        head.next = None
        while k is not None:
            j.next = i
            i = j
            j = k
            k = k.next
        j.next = i
        return j