class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        def dfs(i, j, prev, visited):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]) or heights[i][j] < prev or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i+1, j, heights[i][j], visited)
            dfs(i-1, j, heights[i][j], visited)
            dfs(i, j+1, heights[i][j], visited)
            dfs(i, j-1, heights[i][j], visited)

        for row in range(len(heights)):
            dfs(row, 0, heights[row][0], pac)
            dfs(row, len(heights[0])-1, heights[row][-1], atl)

        for col in range(len(heights[0])):
            dfs(0, col, heights[0][col], pac)
            dfs(len(heights)-1, col, heights[-1][col], atl)

        return [[i, j] for i, j in pac & atl]