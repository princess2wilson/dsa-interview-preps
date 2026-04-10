class Solution:
    import heapq
    from collections import defaultdict,deque
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        N = len(routes) #how many routes
        result = 0
        busvisited = set()
        stopvisited = set()
        queue = deque()

        if source == target:
            return 0
        for bus,stops in enumerate(routes):
            for stop in stops:
                graph[stop].append(bus)
        

        queue.append((source,0))

        while queue:
            stop,result = queue.popleft()
            if stop == target:
                return result
            for bus in graph[stop]:
                if bus not in busvisited:
                    busvisited.add(bus)
                    for stop in routes[bus]:
                        if stop not in stopvisited:
                            stopvisited.add(stop)
                            queue.append((stop,result+1))
            

        return -1




        