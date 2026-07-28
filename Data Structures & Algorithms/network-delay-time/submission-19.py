import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float("inf")]*(n+1)
        graph = defaultdict(list)
        queue = [(0,k)]
        distance[k] = 0

        for src,dst,cost in times:
            graph[src].append((dst,cost))
        
        while queue:
            cost,src = heapq.heappop(queue)

            for dst,next_cost in graph[src]:
                new_cost = cost+next_cost
                if new_cost < distance[dst]:
                    distance[dst] = new_cost
                    heapq.heappush(queue,(new_cost,dst))
        
        
        max_d = 0

        for dist in range(1,n+1):
            max_d = max(max_d,distance[dist])
        return max_d if max_d!=float("inf") else -1
        
        


