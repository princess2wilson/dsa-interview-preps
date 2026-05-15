import sys
sys.setrecursionlimit(15000)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for dx, dy in directions:
                ni, nj = i+dx, j+dy
                if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))
            dp[(i, j)] = res
            return res

        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans = max(ans, dfs(row, col))
        return ans