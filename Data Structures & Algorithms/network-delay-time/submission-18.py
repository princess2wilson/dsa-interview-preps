from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = {item:float("inf") for item in range(n+1)}
        distance[k] = 0
        graph = defaultdict(list)
        queue = [(0,k)]
        max_dis = 0
        for node,nei,weight in times:
            graph[node].append([nei,weight])

        
        while queue:
            current_dist,current_node = heapq.heappop(queue)
            if current_dist > distance[current_node]:
                continue
            for node,distance_ in graph[current_node]:
                new_distance = current_dist+distance_
                if new_distance < distance[node]:
                    distance[node] = new_distance
                    heapq.heappush(queue,(new_distance,node))
        
        max_dis = max(distance[i] for i in range(1, n+1))

        if max_dis == float("inf"):
            return -1
        return max_dis
                    

        

        