class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result = []
        visited = set()
        par = list(range(m*n))
        rank = [1] * (m*n)
        self.count = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def find(x):
            if x!=par[x]:
                par[x] = find(par[x])
            return par[x]
        
        def union(x,y):
            px,py = find(x),find(y)

            if px == py:
                return 
            if rank[px] > rank[py]:
                par[py] = px
                rank[px]+=rank[py]
            else:
                par[px] = py
                rank[py]+=rank[px]
            self.count-=1
    
        for i,j in positions:
            idx = i*n+j
            if idx in visited:
                result.append(self.count)
                continue
            visited.add(idx)
            self.count+=1 

            for x,y in directions:
                ix,iy = i+x,j+y
                didx = ix*n+iy
                if ix>=0 and ix<m and iy>=0 and iy<n and didx in visited:
                    union(didx,idx)
            result.append(self.count)
        return result
    
                








