class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for x in range(len(nums)):
            res[x] = prefix
            prefix*=nums[x]
        postfix = 1
        for x in range(len(nums)-1,-1,-1):
            res[x]*=postfix
            postfix*=nums[x]
        return res


        

             

