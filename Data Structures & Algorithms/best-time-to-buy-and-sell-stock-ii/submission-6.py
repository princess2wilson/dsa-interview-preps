class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cols = 2
        rows = len(prices)
        dp = [[0] * cols for _ in range(rows+1)]
        for ind in range(rows-1,-1,-1):
           dp[ind][1] = max(-prices[ind]+dp[ind+1][0],dp[ind+1][1])
           dp[ind][0] = max(prices[ind]+dp[ind+1][1],dp[ind+1][0])
        return dp[0][1]
            
            