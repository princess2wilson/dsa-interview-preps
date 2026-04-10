class Solution:
    from collections import defaultdict
    import heapq
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        distance = {i:0 for i in range(n)}
        distance[start_node] = 1
        visited=set()

        for x in range(len(edges)):
            u,v = edges[x]
            graph[u].append((v,succProb[x]))
            graph[v].append((u,succProb[x]))



        queue = [(-1,start_node)]

        while queue:
            (current_distance, current_node) = heapq.heappop(queue)
            current_distance *=-1
            if current_node in visited:
                continue
            visited.add(current_node)    
            for node,distance_ in graph[current_node]:
                if node in visited:
                    continue
                new_distance = current_distance*distance_
                if new_distance>distance[node]:
                    distance[node] = new_distance
                    heapq.heappush(queue,(-new_distance,node))
        return distance[end_node]
