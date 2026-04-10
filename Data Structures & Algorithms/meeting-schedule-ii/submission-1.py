"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])

        count = max_count = 0
        p1 = 0
        p2 = 0

        while p1 < len(intervals):
            if start[p1] >= end[p2]:
                count-=1
                p2+=1
            else:
                count+=1
                p1+=1
            max_count = max(count,max_count)
        return max_count

        

