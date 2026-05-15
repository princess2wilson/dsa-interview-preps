import sys
sys.setrecursionlimit(15000)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j, prev):
            if i<0 or i>=ROWS or j<0 or j>=COLS or matrix[i][j]<=prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                res = max(res, 1 + dfs(i+dx, j+dy, matrix[i][j]))
            dp[(i, j)] = res
            return res

        ans = 0
        for row in range(ROWS):
            for col in range(COLS):
                ans = max(ans, dfs(row, col, -1))
        return ans