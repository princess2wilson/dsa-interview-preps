class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visited or grid[i][j]!="1":
                return
            visited.add((i,j))
            for xi,yj in directions:
                dfs(i+xi,j+yj)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col]=="1":
                    dfs(row,col)
                    count+=1
        return count

            