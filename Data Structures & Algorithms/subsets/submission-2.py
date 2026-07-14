class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(ind,temp):
            if ind>=len(nums):
                res.append(temp[:])
                return
            
            
            temp.append(nums[ind])
            take = recurse(ind+1,temp)
            temp.pop()
            no_take = recurse(ind+1,temp)
        recurse(0,[])
        return res
