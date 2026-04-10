class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        left= 0
        right = len(nums) -1
        nums.sort()
        res= 0 
        mod = 10**9 + 7

        while left <= right:
            if nums[right] + nums[left] <= target :
                res = (res + pow(2, right - left, mod)) % mod
                left+=1
            else:
                right-=1
           

        return res

       

    