# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p = list1
        q = list2

        if not p and not q:
            return p

        elif not p and q:
            new_head = ListNode(q.val)
            q = q.next
        
        elif not q and p:
            new_head = ListNode(p.val)
            p = p.next

        elif p.val < q.val:
            new_head = ListNode(p.val)
            p = p.next
        
        elif p.val >= q.val:
            new_head = ListNode(q.val)
            q = q.next

        ptr = new_head

        while p and q:

            if p.val < q.val :
                ptr.next = ListNode(p.val)
                p = p.next
                ptr = ptr.next
        
            else:
                ptr.next = ListNode(q.val)
                q = q.next
                ptr = ptr.next
        
        while p:
            ptr.next = ListNode(p.val)
            p = p.next
            ptr = ptr.next
        
        while q:
            ptr.next = ListNode(q.val)
            q = q.next
            ptr = ptr.next

        return new_head