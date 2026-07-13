class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rows = len(prices)
        next0,next1 = 0,0
        for ind in range(rows-1,-1,-1):
           curr1 = max(-prices[ind]+next0,next1)
           curr0 = max(prices[ind]+next1,next0)
           next0,next1 = curr0,curr1
        return next1
            
            