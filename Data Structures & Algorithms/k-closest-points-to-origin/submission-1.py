import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []

        def get_distance(x1,y1,x2,y2):
            #sqrt((x1 - x2)^2 + (y1 - y2)^2))
            a = (x1 - x2)**2
            b = (y1 - y2)**2
            return (a+b)**0.5
        
        for a,b in points:
            distance = get_distance(0,0,a,b)
            heapq.heappush(queue,(-distance,a,b))

            if len(queue)>k:
                heapq.heappop(queue)
        ans = []
        while queue:
            distance,a,b = heapq.heappop(queue)
            ans.append([a,b])
        return ans
        
