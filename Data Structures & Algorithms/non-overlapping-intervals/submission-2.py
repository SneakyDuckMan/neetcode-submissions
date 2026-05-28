class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        endVal = intervals[0][1]
        removed = 0

        for start, end in intervals[1:]:

            if start < endVal:
                removed += 1
                endVal = min(endVal, end)
            
            else:
                endVal = end
            
        return removed