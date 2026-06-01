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
        intervals.sort(key = lambda x:x.start)

        queue = []
        print(queue)
        
        for x in intervals: 
            if queue and queue[0] <= x.start:
                heapq.heappop(queue)
            heapq.heappush(queue,x.end)
        print(queue)
        return len(queue)
            