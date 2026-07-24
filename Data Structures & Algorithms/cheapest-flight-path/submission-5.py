from collections import defaultdict,deque
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source,dest,cost in flights:
            graph[source].append((dest,cost))
        

        distance = [[float("inf")] * (k + 2) for _ in range(n)]
        distance[src][0] = 0
       
        visited = set()
        queue = []
        heapq.heappush(queue,(0,src,0))


        while queue:
            current_distance,node,cost = heapq.heappop(queue)
            if dst == node:
                return current_distance
            if cost>k:
                continue
            for nei,nei_distance in graph[node]:
                new_distance = current_distance+nei_distance
                if new_distance < distance[nei][cost + 1]:
                    distance[nei][cost+1] = new_distance
                    heapq.heappush(queue,(new_distance,nei,cost+1))
        return -1
    

            



