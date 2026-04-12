class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = set()
        count = 0
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
            
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                count+=1
        return count
       
            
        
            
        
        