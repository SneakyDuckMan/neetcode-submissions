# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        p = head

        while p:
            size += 1
            p = p.next

        if size == 1:
            return None

        p = head
        for i in range(size - n - 1):
            p = p.next

        if size - n - 1 == -1:
            return p.next

        p.next = p.next.next

        return head

        
