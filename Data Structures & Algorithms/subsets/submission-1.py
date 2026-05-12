class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp =[]
        self.helper(0,temp,res,nums)
        return res

    def helper(self,start,temp,res,nums):
        res.append(temp[:])

        for i in range(start,len(nums)):
            temp.append(nums[i])
            self.helper(i+1,temp,res,nums)
            temp.pop()