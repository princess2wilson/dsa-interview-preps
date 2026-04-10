class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for index, price in enumerate(prices):
            sell = max(prices[index:])
            res = max((-price + sell),res)
        return res
