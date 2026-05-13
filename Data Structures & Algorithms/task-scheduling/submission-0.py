class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        time = 0
        count = Counter(tasks)

        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        q = deque()

        while heap or q:
            time += 1

            if heap:
                freq = heapq.heappop(heap) + 1

                if freq != 0:
                    q.append([freq, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
            
        return time
             

        

    
