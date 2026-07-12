class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def recurse(prices,buy,ind,dp):
            if ind==len(prices):
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            take = 0
            dont_take = 0
            if buy == 1:
                take = -prices[ind] + recurse(prices,0,ind+1,dp)
                dont_take = recurse(prices,1,ind+1,dp)
            else:
                take = prices[ind] + recurse(prices,1,ind+1,dp)
                dont_take = recurse(prices,0,ind+1,dp)
            dp[ind][buy] = max(take,dont_take)
            return dp[ind][buy]
        cols = 2
        rows = len(prices)
        dp = [[-1] * cols for _ in range(rows)]
        return recurse(prices,1,0,dp)
            