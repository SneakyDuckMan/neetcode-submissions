class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        newInterval = intervals[0]

        for i in range(1, len(intervals)):

            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                newInterval = intervals[i]
            
            elif intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        while ans and ans[-1][1] > newInterval[0]:
            newInterval[0] =  min(ans[-1][0], newInterval[0])
            ans.pop()

        ans.append(newInterval)

        return ans