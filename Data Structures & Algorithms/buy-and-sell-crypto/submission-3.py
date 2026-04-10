class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        res = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[buy] < prices [sell]:
                res = max(profit,res)
            else:
                buy = sell
            sell+=1
        return res

                


