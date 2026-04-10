class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        res = "0"

        for x in range(len(nums)-2):
            if nums[x] == nums[x+1] == nums[x+2]:
                res = max(res,nums[x:x+3])
        return ""if res =="0" else res
            

            
