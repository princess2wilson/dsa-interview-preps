class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        self.helper(temp,res,nums)
        return res
    def helper(self,temp,res,nums):
        if len(temp) == len(nums):
            res.append(temp[:])    
            return
        
        for i in nums:
            if i not in temp:
                temp.append(i)
                self.helper(temp,res,nums)
                temp.pop()