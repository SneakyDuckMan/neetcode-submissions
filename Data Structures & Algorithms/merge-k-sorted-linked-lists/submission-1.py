# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        heap = []
        dummy = ListNode()
        nn = dummy

        i = 0
        for head in lists:
            heapq.heappush(heap, (head.val, i, head))
            i += 1
        
        while heap:
            val, index, min_node = heapq.heappop(heap)
            nn.next = min_node
            nn = nn.next

            if min_node.next is not None:
                heapq.heappush(heap, (min_node.next.val, i, min_node.next))
            
            i += 1
        
        return dummy.next

