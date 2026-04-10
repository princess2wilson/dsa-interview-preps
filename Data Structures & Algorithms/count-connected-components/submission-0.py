class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        visited = set()
        count = 0
        for x in range(len(edges)):
            if edges[x][0] not in graph:
                graph[edges[x][0]] = []
            graph[edges[x][0]].append(edges[x][1])
            if edges[x][1] not in graph:
                graph[edges[x][1]] = []
            graph[edges[x][1]].append(edges[x][0])
        

        def dfs(node,visited,graph):
            if node in visited or node not in graph:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei,visited,graph)
        

        for node in range(n):
            if node not in visited:
                dfs(node,visited,graph)
                count+=1
            
        
        return count

