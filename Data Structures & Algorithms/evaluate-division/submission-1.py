class Solution:
    from collections import defaultdict
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (x,y),val in zip(equations,values):
            graph[x][y] = val
            graph[y][x] = 1.0/val
        

        def dfs(a,b,visited):
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1

            if b in graph[a]:
                return graph[a][b]
            
            for i in graph[a]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i,b,visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[a][i] * temp

            return -1


        result =[]
        for query in queries:
            result.append(dfs(query[0],query[1],set()))
        return result


