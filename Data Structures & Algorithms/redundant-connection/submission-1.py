class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [n for n in range(n+1)]
        rank = [1] * (n+1)
        self.ans = []

        def find(x):
            if x!=par[x]:
                par[x] = find(par[x])
            return par[x]
        
        def union(x,y):
            px,py = find(x),find(y)

            if px==py:
                self.ans.append([x,y])
                return self.ans
            elif rank[px] > rank[py]:
                par[py] = px
                rank[px]+=rank[py]
            else:
                par[px] = py
                rank[py]+=rank[px]
        
        for x,y in edges:
            union(x,y)
        return self.ans[-1]


            
"""
par - [0,1,2,3,4]
px = 
rank - [1,1,1,1]

"""
