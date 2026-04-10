class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        result = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                diff = prices[sell] - prices[buy]
                result = max(result,diff)
            else: #if there is a smaller buy price then discard the previous one!
                buy=sell
            sell+=1
        return result

                


