class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        self.helper(0,res,0,temp,target,nums)
        return res

    def helper(self,start,res,total,temp,target,nums):
        if total == target:
            res.append(temp[:])
            return
        if total > target:
            return
    
        for i in range(start,len(nums)):
            temp.append(nums[i])
            total+=nums[i]
            self.helper(i,res,total,temp,target,nums)
            temp.pop()
            total-=nums[i] 
