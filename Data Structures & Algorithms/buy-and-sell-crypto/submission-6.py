class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell =0,1
        max_profit = 0

        while sell < len(prices):
            if prices[sell] - prices[buy] > 0 :
                profit = prices[sell] - prices[buy]
                max_profit = max(profit,max_profit)
            else:
                buy=sell
            sell+=1
        return max_profit

 #The reason we don’t “just try selling later” is because:

#👉 A bad buy choice should be discarded immediately.
#👉 A lower price always dominates a higher buy price.

#This is a greedy decision.           
