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
        queue = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:

            if queue and queue[0]<=interval.start:
                heapq.heapreplace(queue,interval.end)
            else:
                heapq.heappush(queue,interval.end)
        return len(queue)