class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k_th = k

        for i in range(min(k, len(nums))):
            heapq.heappush(self.heap, nums[i])
        
        for i in range(k, len(nums)):
            
            if nums[i] > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[i])

    def add(self, val: int) -> int:
        
        if len(self.heap) < self.k_th:
            heapq.heappush(self.heap, val)

        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        return self.heap[0]

        
        
