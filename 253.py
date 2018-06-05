# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        intervals.sort(key = lambda x: x.start)
        a = [intervals[0].end]
        for x in range(1, len(intervals)):
            i = 0
            while i < len(a):
                if intervals[x].start >= a[i]:
                    a[i] = intervals[x].end
                    break
                i += 1
            if i == len(a) or a[i] != intervals[x].end:
                a.append(intervals[x].end)
                    
        return len(a)
