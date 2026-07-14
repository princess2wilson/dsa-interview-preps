class Solution:
    def climbStairs(self, n: int) -> int:
        
        def recurse(n):
            if n<0:
                return 0

            if n == 0:
                return 1

            if dp[n]!=-1:
                return dp[n]


            step = recurse(n-1)
            double_step = recurse(n-2)

            dp[n] = step+double_step
            return dp[n]

        dp = [-1] * (n+1)
        recurse(n)
        return dp[n]
        
       