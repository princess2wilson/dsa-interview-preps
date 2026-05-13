import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])

        queue = [intervals[0]]

        for start,end in intervals[1:]:
            if start <=queue[-1][1]:
                queue[-1][1] = max(queue[-1][1],end)
            else:
                queue.append([start,end])
        return queue



