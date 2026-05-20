class DSU:
    def __init__(self,n):
        self.par = list(range(n+1))
        self.rank = [1] * (n+1)
    
    def find(self,x):
        if x!=self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        px,py = self.find(x),self.find(y)

        if px == py:
            return True
        if self.rank[px]>=self.rank[py]:
            self.par[py] = px
            self.rank[px] +=self.rank[py]

        if self.rank[py]>self.rank[px]:
            self.par[px] = py
            self.rank[py] +=self.rank[px]
        return False

        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for a,b in edges:
            if dsu.union(a,b):
                return [a,b]




