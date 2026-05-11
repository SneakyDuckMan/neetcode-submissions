# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = 0
        p = l1
        q = l2
        carry = 0

        new_head = ListNode() 
        new_node = new_head
        while p and q:
            sum_of_nodes = p.val + q.val + carry
            rem = sum_of_nodes % 10
            carry = sum_of_nodes//10

            new_node.next = ListNode(rem)            
            new_node = new_node.next
            p = p.next
            q = q.next
        
        while p:
            sum_of_nodes = p.val + carry
            rem = sum_of_nodes % 10
            carry = sum_of_nodes//10

            new_node.next = ListNode(rem)
            new_node = new_node.next
            p = p.next
        
        while q:
            sum_of_nodes = q.val + carry
            rem = sum_of_nodes % 10
            carry = sum_of_nodes//10

            new_node.next = ListNode(rem)
            new_node = new_node.next
            q = q.next
        
        if carry != 0:
            new_node.next = ListNode(carry)
        
        return new_head.next

        
