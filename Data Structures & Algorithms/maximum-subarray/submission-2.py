class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res , max_current = nums[0],0

        for num in nums:
            if max_current<0:
                max_current = 0
            max_current+=num
            res = max(res,max_current)
        return res