
from collections import defaultdict,deque
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float("inf")] * n
        distance[src] = 0

        graph = defaultdict(list)

        for source,dest,cost in flights:
            graph[source].append([dest,cost])
        
        queue = deque([(0,src,0)])

        while queue:
            cost,src,stops = queue.popleft()
            if stops>k:
                continue
            
            for dest,new_cost in graph[src]:
                next_cost =new_cost+cost
                if next_cost<distance[dest]:
                    distance[dest] = next_cost
                    queue.append((next_cost,dest,stops+1))
        return distance[dst] if distance[dst]!=float("inf") else -1
        
        

            

        
            
        

