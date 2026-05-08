from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list) 
        res = []
        for (a,b), value in zip(equations,values):
            graph[a].append([b,value])
            graph[b].append([a,1/value])
        
        def dfs(src,dst,visited):
            if src not in graph or dst not in graph:
                return -1
            if src == dst:
                return 1
            for neighbour,value in graph[src]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                result = dfs(neighbour,dst,visited)
                if result !=-1:
                    return result*value
            return -1



        for a,b in queries:
            res.append(dfs(a,b,set()))
        return res

            
            
            


                          

