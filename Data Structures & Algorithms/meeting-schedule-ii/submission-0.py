"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        intervals.sort(key = lambda i: (i.start, i.end))
        minHeap = [intervals[0].end]
        ans = 1

        for i in intervals[1:]:
            if i.start >= minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, i.end)
            
            else:
                heapq.heappush(minHeap, i.end)

                ans = max(ans, len(minHeap))

        return ans



