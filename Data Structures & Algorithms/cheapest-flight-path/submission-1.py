class Solution:
    from collections import defaultdict,heapq
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for flight in (flights):
            source = flight[0]
            dest = flight[1]
            cost = flight[2]
            graph[source].append((cost,dest))
        
        costs = {i:float("inf") for i in range(n)}
        stops_record = {i: float("inf") for i in range(n)}
        costs[src] = 0
 

        queue = [(0,src,0)]
        while queue:
            current_cost,current_src,stops = heapq.heappop(queue)

            if stops > k:
                continue 
           
            for cost,next_city in graph[current_src]:
                new_cost = cost+current_cost
                if new_cost < costs[next_city] or stops < stops_record[next_city]:
                    stops_record[next_city] = stops
                    costs[next_city] = new_cost
                    heapq.heappush(queue,(new_cost,next_city,stops+1))
        

        return costs[dst] if costs[dst] != float("inf") else -1

        

            

        
