class Solution:
    from collections import defaultdict
    import heapq
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        queue = []

        for u,v,cost in times:
            graph[u].append((v,cost))

        distance = {i:float("inf") for i in range(1, n + 1)}
        distance[k] = 0 
        queue = [(0,k)]
        previous ={node: None for node in graph}


        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distance[current_node]:
                continue
            for node,distance_ in graph[current_node]:
                new_distance = current_distance+distance_
                if new_distance < distance[node]:
                    distance[node] = new_distance
                    heapq.heappush(queue,(new_distance,node))
               

        ans = max(distance.values())
        return ans if ans < float("inf") else -1