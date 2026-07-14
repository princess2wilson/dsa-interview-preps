class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def recurse(ind,bs):
            if ind>=len(prices):
                return 0
            if bs == 1:
                buy = max(-prices[ind] + recurse(ind+1,0),recurse(ind+1,1))
                return buy
            else:
                sell = max(prices[ind],recurse(ind+1,0))
                return sell
        return recurse(0,1)
