class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def recurse(ind,buy_):
            buy = sell = 0
            if ind>=len(prices):
                return 0
            if dp[ind][buy_]!=-1:
                return dp[ind][buy_]
            if buy_ == 1:
                buy = max(-prices[ind]+recurse(ind+1,0),recurse(ind+1,1))
            else:
                sell = max(prices[ind]+recurse(ind+2,1),recurse(ind+1,0))
            dp[ind][buy_] = buy+sell 
            return dp[ind][buy_]

        dp = [[-1] * 2 for _ in range(len(prices))]
        return recurse(0,1)
