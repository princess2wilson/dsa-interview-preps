class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        profit = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                diff = prices[sell] - prices[buy]
                profit = max(profit,diff)

            else:
                buy = sell
            sell+=1
        
        return profit
 #The reason we don’t “just try selling later” is because:

#👉 A bad buy choice should be discarded immediately.
#👉 A lower price always dominates a higher buy price.

#This is a greedy decision.           
