class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        adj =[[] for t in range(n)] #adj=[[],[],[]]]
        visited = [False] * n #visited = [False,False,False..]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        

        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        
        for node in range(n):
            if not visited[node]:
                #starting node procedure
                visited[node]= True
                dfs(node)
                count+=1
                
            
        
        return count

