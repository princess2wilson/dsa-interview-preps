from collections import defaultdict
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:


        def recursion(i,target):
            if i>=len(coins) or target<0:
                return float("inf")
            if target == 0:
                return 0
            if dp[i][target]!=-1:
                return dp[i][target]
            
            take = 1+recursion(i,target-coins[i])
            dont_take = 0+recursion(i+1,target)

            dp[i][target] = min(take,dont_take)
            return dp[i][target]


        dp = [[-1] * (amount+1) for _ in range(len(coins))]
        res =  recursion(0,amount)

        if res == float("inf"):
            return -1
        else:
            return res
        
