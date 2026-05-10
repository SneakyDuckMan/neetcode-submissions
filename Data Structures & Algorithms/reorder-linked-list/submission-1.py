# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next
        
        rev_i = (size+1)//2 if size % 2 else size//2

        if size == 1:
            return

        q = head
        for i in range(rev_i):
            q = q.next
            if i == rev_i - 2:
                q_prev = q

        q_prev.next = None
        
        q = self.reverse(q)
        p = head

        

        while p and q:
            p_next = p.next
            q_next = q.next
            q.next = p.next
            p.next = q

            p = p_next
            q = q_next
            q_next = q_next.next if q_next else None

    def reverse(self, head):
        p = head
        prev = None

        while p:
            next_node = p.next
            p.next = prev
            prev = p
            p = next_node
        
        return prev

    