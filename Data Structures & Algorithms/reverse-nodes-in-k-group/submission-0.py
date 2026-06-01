# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        start = head
        p = head
        count = 0
        new_head = None

        def reverse(head, prev):
            p = head

            for i in range(k):
                nextNode = p.next
                p.next = prev
                
                prev = p
                p = nextNode
            
            return prev

        while p:
            p = p.next
            count += 1

            if count == k:
                new_head = reverse(start, p)
            
            elif count % k == 0:
                next_start = start.next
                start.next = reverse(next_start, p)
                start = next_start

    
        
        return new_head if new_head else head



