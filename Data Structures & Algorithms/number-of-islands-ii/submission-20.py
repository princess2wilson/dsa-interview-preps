class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU(m,n)
        count = 0
        grid = [[0] * n for _ in range(m)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res = []
                
        for i,j in positions:
            if grid[i][j] == 1:
                res.append(count)
                continue
            grid[i][j] = 1
            count+=1
            
            for x,y in directions:
                dx,dy = i+x,j+y
                if self.pos_check(dx,dy,m,n,grid):
                    id1 = i*n+j
                    id2 = dx*n+dy
                    valid_union = dsu.union(id1,id2)
                    if valid_union:
                        count-=1
            res.append(count)
        return res
    
    def pos_check(self,x,y,m,n,grid):
        if x<0 or x>=m or y<0 or y>=n or grid[x][y] == 0:
            return False
        return True   
                

class DSU:
    def __init__(self,m,n):
        self.par = list(range(m*n))
        self.rank = [1]*(m*n)
    
    def find(self,x):
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)

        if px==py:
            return False #come back to this
        if self.rank[px]>self.rank[py]:
            self.par[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.par[px] = py
            self.rank[py]+=self.rank[px]
        return True

    


        
        










