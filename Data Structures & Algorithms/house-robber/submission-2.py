class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def recurse(ind,dp):
            if ind>=len(nums):
                return 0
            if dp[ind]!=-1:
                return dp[ind]

            rob = nums[ind]+recurse(ind+2,dp)
            dont_rob = 0 + recurse(ind+1,dp)

            dp[ind] =  max(rob,dont_rob)
            return dp[ind]
        dp  = [-1] * len(nums)
        return recurse(0,dp)