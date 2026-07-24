class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        visited = set()
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!="1" or (i,j) in visited:
                return
            visited.add((i,j))
            for x,y in directions:
                dx,dy = x+i,y+j
                dfs(dx,dy)
            
            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1" and (row,col) not in visited:
                    count+=1
                    dfs(row,col)
                    
        return count


