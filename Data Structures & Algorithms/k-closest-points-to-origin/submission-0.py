class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def neg_dist(point):
            x, y = point[0], point[1]

            return -x*x - y*y

        heap = []

        for i, point in enumerate(points):
            
            if i < k:
                heapq.heappush(heap,(neg_dist(point) ,point))
            
            else:
                ndist, far_point = heap[0]

                if neg_dist(point) > ndist:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (neg_dist(point), point))
        
        ans = []

        for ele in heap:
            dist, point = ele
            ans.append(point)
        
        return ans


        