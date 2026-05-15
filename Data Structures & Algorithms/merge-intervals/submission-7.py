class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        arr = [intervals[0]]

        for start,end in intervals[1:]:
            if start<=arr[-1][1]:
                arr[-1][1] = max(end, arr[-1][1])
            else:
                arr.append([start,end])
        return arr


"""
two use cases:
do i start before the last one ends?,
is start <= previous end :
    theres an overlap
if start > previous end :
    non overalp
sort array by start time
1. create an array , youll return this at end
add first one to array and then check. 
f overallping, extend the end time by max of the two
"""
