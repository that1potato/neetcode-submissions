# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]

        pointers = []  # heads of all linked lists
        heapq.heapify(pointers)
        for i, l in enumerate(lists):
            heapq.heappush(pointers, (l.val, i, l)) # i is the tie breaker
        
        # pop min from heap to build the output
        dummy = ListNode()
        cur = ListNode()
        dummy.next = cur
        while pointers:
            value, i, pointer = heapq.heappop(pointers)
            cur.next = pointer
            cur = cur.next
            if pointer.next:
                heapq.heappush(pointers, (pointer.next.val, i, pointer.next))

        return dummy.next.next
