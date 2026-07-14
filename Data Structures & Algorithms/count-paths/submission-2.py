class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def recurse(x,y,dp):
            if x>=m or y>=n:
                return 0
            if x == m-1 and y == n-1:
                return 1
            if dp[x][y] !=-1:
                return dp[x][y]
            right = recurse(x+1,y,dp)
            left = recurse(x,y+1,dp)
            dp[x][y] = right+left
            return dp[x][y]
        dp = [[-1]*(n+1) for _ in range(m+1)]
        return recurse(0,0,dp)