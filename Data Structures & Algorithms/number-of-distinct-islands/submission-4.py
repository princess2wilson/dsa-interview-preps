from collections import defaultdict
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.seen = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        self.temp = []

        def dfs(i,j,previ,prevj):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visited or grid[i][j]==0:
                return False
            visited.add((i,j))
            self.temp.append(((previ-i),(prevj-j)))


            for x,y in directions:
                dx,dy = i+x,j+y
                dfs(dx,dy,previ,prevj)
                
            return True
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.temp = []
                if dfs(row,col,row,col):
                    self.seen.add(tuple(self.temp))
        return len(self.seen)
            



