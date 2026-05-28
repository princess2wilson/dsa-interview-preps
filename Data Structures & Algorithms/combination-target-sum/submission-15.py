class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def helper(start,total,temp):
            nonlocal res
            if total == target:
                res.append(temp[:])
                return
            if total > target:
                return
            

            for i in range(start,len(nums)):
                total+=nums[i]
                temp.append(nums[i])
                helper(i,total,temp) 
                total-=nums[i]
                temp.pop()
        res = []
        helper(0,0,[])
        return res
            