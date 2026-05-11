"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None

        new_head = Node(head.val)
        p = head.next
        curr = new_head
        hashmap = {}
        hashmap[head] = new_head

        while p:
            curr.next = Node(p.val)
            curr = curr.next
            hashmap[p] = curr
            p = p.next
            
        p = head
        curr = new_head

        while p:
            curr.random = hashmap[p.random] if p.random else None
            p = p.next
            curr = curr.next
        
        return new_head
