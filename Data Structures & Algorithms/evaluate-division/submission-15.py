from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a,b),val in zip(equations,values):
            graph[a].append([b,val])
            graph[b].append([a,1/val])

        def dfs(src,dst,visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            for neighbour, val in graph[src]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    res = dfs(neighbour,dst,visited)
                    if res != -1:
                        return res*val
            return -1
            

        arr = []
        for a,b in queries:
            arr.append(dfs(a,b,set()))
        return arr

           