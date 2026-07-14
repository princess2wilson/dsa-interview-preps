class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def recurse(ind,bs,dp):

            if ind>=len(prices):
                return 0
            if dp[ind][bs]!=-1:
                return dp[ind][bs]
                
            if bs == 1:
                dp[ind][bs] = max(-prices[ind] + recurse(ind+1,0,dp),recurse(ind+1,1,dp))
                return dp[ind][bs]
            else:
                dp[ind][bs] = max(prices[ind],recurse(ind+1,0,dp))
                return dp[ind][bs]
        dp = [[-1] * 2 for _ in range(len(prices))]
        return recurse(0,1,dp)
       
