"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        temp = []
        count = 0 
        if len(intervals)==0:
            return 0


        for x in intervals:
            if temp and temp[0] <= x.start:
                heapq.heapreplace(temp,x.end)
            else:
                heapq.heappush(temp,(x.end))
        return len(temp)
