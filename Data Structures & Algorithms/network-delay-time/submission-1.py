class Solution:
    from collections import deque,defaultdict
    import heapq
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        queue = []
        graph = defaultdict(list)
        start = (0,k)
        distance = {item:float("inf") for item in range(n+1)}
        distance[k] = 0
        for time in times:
            graph[time[0]].append([time[2],time[1]])

        heapq.heappush(queue,start)

        while queue:
            current_distance,current_node = heapq.heappop(queue)
            if current_distance > distance[current_node]:
                continue
            for weight,node in graph[current_node]:
                new_distance = current_distance+weight
                if new_distance < distance[node]:                 
                    distance[node] = new_distance
                    heapq.heappush(queue,(new_distance,node))
        
        result = max(distance[i] for i in range(1, n+1))
        return -1 if result == float("inf") else result



