class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        ans =[]

        x=1
        for i in range(len(nums)):
            prefix[i]=x
            x*=nums[i]

        x=1
        for i in range(len(nums)-1,-1,-1):
            postfix[i] *= x
            x *= nums[i]

        x=1
        for i in range(len(nums)):
            ans.append(prefix[i]*postfix[i])
        return ans

        

             

