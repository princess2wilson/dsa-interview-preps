class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        def recurse(prices,buy,ind,dp):
            if ind==len(prices):
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy == 1:
                profit = max(-prices[ind]+recurse(prices,0,ind+1,dp),recurse(prices,1,ind+1,dp))
            else:
                profit = max(prices[ind]+recurse(prices,1,ind+1,dp),recurse(prices,0,ind+1,dp))

            dp[ind][buy] = profit
            return dp[ind][buy]
        cols = 2
        rows = len(prices)
        dp = [[-1] * cols for _ in range(rows)]
        return recurse(prices,1,0,dp)
            