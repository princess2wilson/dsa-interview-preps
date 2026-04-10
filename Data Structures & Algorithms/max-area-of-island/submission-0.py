class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        def dfs(r,c):
            if r < 0 or r == rows or c < 0 or c == columns or grid[r][c] == 0 :
                return 0
            
            grid[r][c] = 0 #mark as visited
             
            count = (1 + dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
            return count

        area = 0
        for r in range(rows):
            for c in range(columns):
                count =dfs(r,c)
                area = max(area, count)
        return area
                
                    