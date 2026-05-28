class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(0,0,nums,res,[],target)
        return res

    def helper(self,start,total,nums,res,temp,target):
        if total == target:
            res.append(temp[:])
            return 
        if total > target:
            return
        
        for i in range(start,len(nums)):
            total+=nums[i]
            temp.append(nums[i])
            self.helper(i,total,nums,res,temp,target)
            temp.pop()
            total-=nums[i]

            