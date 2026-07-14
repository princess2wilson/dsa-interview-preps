class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(ind,target,temp):
            if target<0 or ind>=len(nums):
                return
            if target == 0:
                res.append(temp[:])
                return

            temp.append(nums[ind])
            take = backtrack(ind,target-nums[ind],temp)
            temp.pop()
            no_take = backtrack(ind+1,target,temp)
        backtrack(0,target,[])
        return res