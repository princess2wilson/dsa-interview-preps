class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        perim = 0
        visited = set()

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=columns or grid[i][j] == 0 :
                return 1
            if (i,j) in visited:
                return 0
            
            visited.add((i,j))

            perim = (dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1))
            return perim
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]:
                    return(dfs(r,c))
        return 0
