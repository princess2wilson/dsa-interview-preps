class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1 = 0
        total = 0
        res = float('inf')

        for p2 in range(len(nums)):
            total+=nums[p2]
            
            while total>=target:
                res = min(res,p2+1-p1)
                total-=nums[p1]
                p1+=1
        if res == float('inf'):
            return 0
        else:
            return res        
