# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        dummy = ListNode(next=head)
        fast = head
        slow = dummy
        while not fast == slow:
            if fast.next is not None:
                fast = fast.next
                if fast.next is not None:
                    fast = fast.next
                else:
                    return False
            else:
                return False
            
            slow = slow.next

        return True