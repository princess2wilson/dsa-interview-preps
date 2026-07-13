class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cols = 2
        rows = len(prices)+1
        dp = [[0] * cols for _ in range(rows)]
        dp[rows-1][0] = dp[rows-1][1] = 0
        for ind in range(rows-2,-1,-1):
            for buy in range(2):
                if buy == 1:
                    profit = max(-prices[ind]+dp[ind+1][0],dp[ind+1][1])
                else:
                    profit = max(prices[ind]+dp[ind+1][1],dp[ind+1][0])

                dp[ind][buy] = profit
        return dp[0][1]
            
            