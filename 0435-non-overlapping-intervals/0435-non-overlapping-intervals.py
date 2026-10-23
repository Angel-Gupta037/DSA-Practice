class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        cnt=0
        prev=intervals[0][1]
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            if start<prev:
                cnt+=1
            else:
                prev=end
        return cnt
        