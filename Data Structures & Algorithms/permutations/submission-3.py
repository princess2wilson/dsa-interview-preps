class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        visited = set()
        self.helper(temp,res,nums,visited)
        return res
    def helper(self,temp,res,nums,visited):
        if len(temp) == len(nums):
            res.append(temp[:])    
            return
        
        for i in nums:
            if i not in visited:
                visited.add(i)
                temp.append(i)
                self.helper(temp,res,nums,visited)
                temp.pop()
                visited.remove(i)