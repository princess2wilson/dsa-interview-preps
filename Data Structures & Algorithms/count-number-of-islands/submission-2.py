class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visited or grid[i][j]!="1":
                return

            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col)not in visited:
                    dfs(row,col)
                    count+=1
        return count    