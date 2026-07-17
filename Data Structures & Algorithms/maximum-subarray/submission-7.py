class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_arr = float("-inf")
        curr_max = 0


        for r in range(len(nums)):
            curr_max+=nums[r]
            max_arr = max(max_arr,curr_max)
            if curr_max<0:
                curr_max=0
        return max_arr

