"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        count = 0

        if len(intervals)==0:
            return 0
        queue = []

        for x in intervals:
            if queue and x.start >= queue[0]:
                count+=1
                heapq.heapreplace(queue,x.end)
            else:
                heapq.heappush(queue,x.end)
        return len(queue)



        
        