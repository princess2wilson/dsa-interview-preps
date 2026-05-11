class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        r= intervals[0][1]
        count = 0



        for start,end in intervals[1:]:
            if start >=r:
                r = end
            else:
                count+=1
        return count
