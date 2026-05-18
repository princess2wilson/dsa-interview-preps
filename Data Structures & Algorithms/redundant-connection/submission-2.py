class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [n for n in range(n+1)]
        rank = [1] * (n+1)

        def find(x):
            if x!=par[x]:
                par[x] = find(par[x])
            return par[x]
        
        def union(x,y):
            px,py = find(x),find(y)

            if px==py:
                return False
            elif rank[px] > rank[py]:
                par[py] = px
                rank[px]+=rank[py]
            else:
                par[px] = py
                rank[py]+=rank[px]
            return True
        
        for x,y in edges:
            if not union(x,y):
                return [x,y]


            
"""
par - [0,1,2,3,4]
px = 
rank - [1,1,1,1]

"""
