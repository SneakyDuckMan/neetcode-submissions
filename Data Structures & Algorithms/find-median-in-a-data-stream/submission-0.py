class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        
        if not self.max_heap:
            self.max_heap.append(-num)
            return
        
        if num > -self.max_heap[0]:
            heapq.heappush(self.min_heap, num)
        
        else:
            heapq.heappush(self.max_heap, -num)
        
        while len(self.max_heap) - len(self.min_heap) > 1:

            n = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, n)
        
        while len(self.min_heap) - len(self.max_heap) > 0:

            n = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -n)

    def findMedian(self) -> float:

        if (len(self.max_heap) + len(self.min_heap))% 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0])/2
        
        else:
            return float(-self.max_heap[0])
        
        