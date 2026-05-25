class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        self.count = 0
        grid = [[0]*n for _ in range(m)]
        dsu = DSU(n,m)
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        arr = []
        for a,b in positions:
            if grid[a][b] == 1:
                arr.append(dsu.count)
                continue
            id1 = (a*n)+b
            grid[a][b]=1
            dsu.count+=1
            for x,y in directions:
                ax,by = a+x,b+y
                if ax<0 or ax>=m or by<0 or by>=n or grid[ax][by]!=1:
                    continue
                #inbound check here and ==1 check
                id2 = (ax*n) + by
                dsu.union(id1,id2)
            arr.append(dsu.count)
        return arr

class DSU:
    def __init__(self,n,m):
        identity = m*n
        self.par = list(range(identity))
        self.rank = [1] * (identity)
        self.count = 0

    def find(self,x):
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        
        if px==py:
            return
        if self.rank[px] > self.rank[py]:
            self.par[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.par[px] = py
            self.rank[py]+=self.rank[px]
        self.count-=1
    



        

    


