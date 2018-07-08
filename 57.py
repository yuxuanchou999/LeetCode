# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i, res = 0, []
        while i < len(intervals):
            if intervals[i].start <= newInterval.start <= intervals[i].end:
                start = intervals[i].start
                i += 1
                while i < len(intervals) and newInterval.end >= intervals[i].start:
                    i += 1
                res.append(Interval(start, max(newInterval.end, intervals[i - 1].end)))
                res += intervals[i:]
                return res
            elif newInterval.start < intervals[i].start:
                while i < len(intervals) and newInterval.end >= intervals[i].start:
                    i += 1
                if i:
                    res.append(Interval(newInterval.start, max(newInterval.end, intervals[i - 1].end)))
                else:
                    res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                res.append(intervals[i])
                i += 1
        intervals.append(newInterval)
        return intervals
            
        
        
            
                    s
