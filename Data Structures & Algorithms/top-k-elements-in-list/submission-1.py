class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        heap = []

        for i,num in enumerate(counts):
            if i < k:
                heapq.heappush(heap, (counts[num], num))
                continue

            min_count, n = heap[0]

            if min_count < counts[num]:
                heapq.heappop(heap)
                heapq.heappush(heap, (counts[num], num))
        
        ans = []
        for ele in heap:
            count, num = ele
            ans.append(num)

        print(heap)
        return ans
        

