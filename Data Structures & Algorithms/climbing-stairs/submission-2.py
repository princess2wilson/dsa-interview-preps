class Solution:
    def climbStairs(self, n: int) -> int:
        
        def recurse(n,dp):
            if n<0:
                return 0

            if n == 0:
                return 1

            if dp[n]!=-1:
                return dp[n]


            step = recurse(n-1,dp)
            double_step = recurse(n-2,dp)

            dp[n] = step+double_step
            return dp[n]

        dp = [-1] * (n+1)
        recurse(n,dp)
        return dp[n]
        
       